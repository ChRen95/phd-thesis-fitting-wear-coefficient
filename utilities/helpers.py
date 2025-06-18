import json
import numpy as np
import pyroll.core as pr
import matplotlib.pyplot as plt

from pathlib import Path
from shapely import LineString
from scipy.interpolate import interp1d
from scipy.integrate import simpson

from .roll_pass import pillar_wear_depths

def extract_wear_contours_from_measurement(groove_name):
    root_dir = Path.cwd()
    wear_data_dir = root_dir / "wear_data" / groove_name

    measurements = []

    for file in wear_data_dir.iterdir():
        with open(file, "r") as f:
            data = json.load(f)

        labels = []
        tonnages = []
        measured_wear_contours = []

        for entry in data["wear_data"]:
            labels.append(entry["stand"])
            tonnages.append(entry["tonnage"])
            z_values = np.array([point["x"] for point in entry["wear_contour"]])
            y_values = np.array([point["y"] for point in entry["wear_contour"]])
            contour = LineString(list(zip(z_values, y_values)))
            measured_wear_contours.append(contour)

        measurement_id = file.stem
        measurements.append((measurement_id, labels, tonnages, measured_wear_contours))

    return measurements


def calculate_area_between_contours(contour_1: LineString, contour_2: LineString, debug: bool = False):
    z1, y1 = contour_1.xy
    z2, y2 = contour_2.xy

    z_min = max(min(z1), min(z2))
    z_max = min(max(z1), max(z2))
    z_common = np.linspace(z_min, z_max, 1000)

    f1 = interp1d(z1, y1, kind='linear', fill_value='extrapolate')
    f2 = interp1d(z2, y2, kind='linear', fill_value='extrapolate')

    y1_interp = f1(z_common)
    y2_interp = f2(z_common)

    if debug:
        fig, ax = plt.subplots()
        ax.plot(z1, y1, label="Contour 1")
        ax.plot(z2, y2, label="Contour 2")
        ax.plot(z_common, y1_interp, label="Interpolated - C1 - Common")
        ax.plot(z_common, y1_interp, label="Interpolated - C2 - Common")

    diff = np.abs(y1_interp - y2_interp)
    area = simpson(diff, z_common)

    return area


def root_mean_square_value(error_array: np.array) -> float:
    return np.sqrt(np.mean(error_array ** 2))


def calculate_wear_contour(roll_pass: pr.RollPass, wear_coefficient: float, tonnage: float):

    calculated_wear_contour = pillar_wear_depths(roll_pass, wear_coefficient, tonnage) + roll_pass.roll.groove.local_depth(roll_pass.out_profile.pillars)

    right_side = list(zip(roll_pass.out_profile.pillars, calculated_wear_contour))
    left_side = list(zip(-roll_pass.out_profile.pillars[::-1], calculated_wear_contour[::-1]))
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
