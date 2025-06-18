import numpy as np
import pyroll.core as pr

VICKERS_HARDNESS_C15C = 900

def pillar_deformation_resistance(roll_pass: pr.RollPass):
    from pyroll.freiberg_flow_stress import flow_stress
    pillars_flow_stress = flow_stress(roll_pass.out_profile.freiberg_flow_stress_coefficients,
                                      roll_pass.total_pillar_strains,
                                      roll_pass.total_pillar_strain_rates,
                                      roll_pass.out_profile.temperature)
    return pillars_flow_stress / roll_pass.rolling_efficiency


def pillars_wear_length(roll: pr.RollPass.Roll) -> np.ndarray:
    local_roll_radii = np.concatenate(
        [roll.max_radius - roll.surface_interpolation(0, center)
         for center in roll.roll_pass.in_profile.pillars],
        axis=0).flatten()

    _pillars_wear_length = np.zeros_like(roll.roll_pass.in_profile.pillars)

    for de in roll.roll_pass.disk_elements:
        horizontal_roll_velocities = local_roll_radii * roll.rotational_frequency * 2 * np.pi * np.cos(
            de.pillar_longitudinal_angles)
        for i, pillars in enumerate(de.in_profile.pillars):
            if de.pillar_velocities[i] < horizontal_roll_velocities[i] and de.pillars_in_contact[i]:
                _pillars_wear_length[i] += de.length

    return _pillars_wear_length


def pillar_wear_depths(roll_pass: pr.RollPass, wear_coefficient: float, tonnage):

    _pillars_wear_length = pillars_wear_length(roll_pass.roll)
    _pillar_deformation_resistance = pillar_deformation_resistance(roll_pass)

    return wear_coefficient * _pillar_deformation_resistance * _pillars_wear_length / (
                3 * VICKERS_HARDNESS_C15C) *  tonnage / roll_pass.in_profile.weight