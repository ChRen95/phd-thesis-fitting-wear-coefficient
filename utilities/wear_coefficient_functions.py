import pyroll.core as pr


def get_wear_coefficient(roll_pass: pr.RollPass, params: dict):
    if "wear_coefficient" in params:
        _wear_coefficient = params["wear_coefficient"].value
    elif "speed_ratio_coefficient" in params:
        _wear_coefficient = wear_coefficient_cubic(roll_pass, params["base_wear_coefficient"].value,
                                                   params["roll_gap_ratio_coefficient"].value,
                                                   params["speed_ratio_coefficient"].value)
    else:
        _wear_coefficient = wear_coefficient_linear(roll_pass, params["base_wear_coefficient"].value,
                                                    params["roll_gap_ratio_coefficient"].value)

    return _wear_coefficient

def calculate_roll_gap_ratio(roll_pass: pr.RollPass):
    mean_cross_section = (roll_pass.in_profile.cross_section.area + 2 * roll_pass.out_profile.cross_section.area) / 3
    return roll_pass.roll.contact_area / mean_cross_section


def wear_coefficient_linear(roll_pass: pr.RollPass, base_wear_coefficient: float, roll_gap_ratio_coefficent: float):
    roll_gap_ratio = calculate_roll_gap_ratio(roll_pass)

    return base_wear_coefficient + roll_gap_ratio * roll_gap_ratio_coefficent


def wear_coefficient_cubic(roll_pass: pr.RollPass, base_wear_coefficient: float, roll_gap_ratio_coefficient: float,
                           speed_ratio_coefficient: float):
    speed_ratio = roll_pass.velocity / roll_pass.in_profile.velocity
    roll_gap_ratio = calculate_roll_gap_ratio(roll_pass)

    return base_wear_coefficient + roll_gap_ratio * roll_gap_ratio_coefficient + speed_ratio * speed_ratio_coefficient ** 2
