import json
import numpy as np
import pyroll.core as pr

from pathlib import Path
from shapely import LineString
from scipy.interpolate import interp1d
from scipy.integrate import simpson


def pillar_deformation_resistance(roll_pass: pr.RollPass):
    from pyroll.freiberg_flow_stress import flow_stress
    pillars_flow_stress = flow_stress(roll_pass.out_profile.freiberg_flow_stress_coefficients,
                                      roll_pass.total_pillar_strains,
                                      roll_pass.total_pillar_strain_rates,
                                      roll_pass.out_profile.temperature)
    pillar_deformation_resistance = pillars_flow_stress / roll_pass.rolling_efficiency
    return pillar_deformation_resistance


def pillars_wear_length(roll: pr.RollPass.Roll) -> np.ndarray:
    local_roll_radii = np.concatenate(
        [roll.max_radius - roll.surface_interpolation(0, center)
         for center in roll.roll_pass.in_profile.pillars],
        axis=0).flatten()

    pillars_wear_length = np.zeros_like(roll.roll_pass.in_profile.pillars)

    for de in roll.roll_pass.disk_elements:
        horizontal_roll_velocities = local_roll_radii * roll.rotational_frequency * 2 * np.pi * np.cos(
            de.pillar_longitudinal_angles)
        for i, pillars in enumerate(de.in_profile.pillars):
            if de.pillar_velocities[i] < horizontal_roll_velocities[i] and de.pillars_in_contact[i]:
                pillars_wear_length[i] += de.length

    return pillars_wear_length


def extract_wear_contours_from_measurement(groove_name):
    root_dir = Path.cwd()
    wear_data_dir = root_dir / "wear_data" / groove_name

    labels = []
    tonnages = []
    measured_wear_contours = []

    for file in wear_data_dir.iterdir():
        with open(file, "r") as file:
            data = json.load(file)

        for entry in data["wear_data"]:
            labels.append(entry["stand"])
            tonnages.append(entry["tonnage"])
            x_values = np.array([point["x"] * 1e-3 for point in entry["wear_contour"]])
            y_values = np.array([point["y"] * 1e-3 for point in entry["wear_contour"]])
            x_values_shifted = x_values - max(x_values) / 2
            measured_wear_contour = LineString(list(zip(x_values_shifted, y_values)))
            measured_wear_contours.append(measured_wear_contour)

        return labels, tonnages, measured_wear_contours


def calculate_area_between_contours(contour_1: LineString, contour_2: LineString):
    z1, y1 = contour_1.xy
    z2, y2 = contour_2.xy
    z_min = max(min(z1), min(z2))
    z_max = min(max(z1), max(z2))
    z_common = np.linspace(z_min, z_max, 1000)

    f1 = interp1d(z1, y1, kind='linear', fill_value='extrapolate')
    f2 = interp1d(z2, y2, kind='linear', fill_value='extrapolate')

    y1_interp = f1(z_common)
    y2_interp = f2(z_common)

    diff = np.abs(y1_interp - y2_interp)
    area = simpson(diff, z_common)

    return area


def root_mean_square_value(error_array: np.array) -> float:
    return np.sqrt(np.mean(error_array ** 2))


def calculate_wear_contour(roll_pass: pr.RollPass, wear_coefficient: float, tonnage: float):
    vickers_hardness_c15c = 900

    _pillars_wear_length = pillars_wear_length(roll_pass.roll)
    _pillar_deformation_resistance = pillar_deformation_resistance(roll_pass)
    pillar_wear_depths = wear_coefficient * _pillar_deformation_resistance * _pillars_wear_length / (
            3 * vickers_hardness_c15c)
    total_pillar_wear_depths = pillar_wear_depths * tonnage / roll_pass.in_profile.weight
    wear_depths_with_groove_contour = roll_pass.roll.groove.local_depth(
        roll_pass.out_profile.pillars) + total_pillar_wear_depths
    right_side = list(zip(roll_pass.out_profile.pillars, wear_depths_with_groove_contour))
    left_side = list(zip(-roll_pass.out_profile.pillars[::-1], wear_depths_with_groove_contour[::-1]))
    combined_contour_list = left_side + right_side
    wear_contour = LineString(combined_contour_list)

    return wear_contour


def compare_groove_contour_to_wear_contour(sequence: pr.PassSequence, roll_pass_label: str):
    for roll_pass in sequence.roll_passes:
        if roll_pass.label == roll_pass_label:
            groove = roll_pass.roll.groove

    labels, tonnages, measured_wear_contours = extract_wear_contours_from_measurement(roll_pass_label)

    areas_between_contours = []
    for contour in measured_wear_contours:
        area = calculate_area_between_contours(contour, groove.contour_line)
        areas_between_contours.append(area)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title("Groove Contour Comparison")
    ax.plot(*groove.contour_line.xy)
    for contour, tonnage, label, area in zip(measured_wear_contours, tonnages, labels, areas_between_contours):
        ax.plot(*contour.xy, label=f"{label} - {tonnage}")
        print(f"Area between original groove and wear contour after {tonnage} tons: {area * 1e6:.6e} mm²")
    ax.set_xlabel("z [m]")
    ax.set_ylabel("y [m]")
    ax.set_aspect("equal")
    ax.legend()
    ax.grid(True)

    return np.array(areas_between_contours)
