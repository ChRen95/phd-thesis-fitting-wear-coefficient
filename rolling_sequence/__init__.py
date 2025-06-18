import pyroll.core as pr

from .roughing_train import roughing_sequence
from .intermediate_train import intermediate_sequence
from .finishing_train import finishing_pass_design_1, finishing_pass_design_2, finishing_pass_design_3


def rolling_train_rpd1(roll_surface_temperature: float, disk_element_count: int):
    roughing_train = roughing_sequence(
        roll_surface_temperature=roll_surface_temperature,
        disk_element_count=disk_element_count
    )

    intermediate_train = intermediate_sequence(
        roll_surface_temperature=roll_surface_temperature,
        disk_element_count=disk_element_count
    )

    finishing_train_e112 = finishing_pass_design_1(
        roll_surface_temperature=roll_surface_temperature,
        disk_element_count=disk_element_count
    )

    sequence = pr.PassSequence([
        roughing_train,
        intermediate_train,
        finishing_train_e112
    ])

    sequence.flatten()

    return sequence


def rolling_train_rpd2(roll_surface_temperature: float, disk_element_count: int):
    roughing_train = roughing_sequence(
        roll_surface_temperature=roll_surface_temperature,
        disk_element_count=disk_element_count
    )

    intermediate_train = intermediate_sequence(
        roll_surface_temperature=roll_surface_temperature,
        disk_element_count=disk_element_count
    )

    finishing_train_e107 = finishing_pass_design_2(
        roll_surface_temperature=roll_surface_temperature,
        disk_element_count=disk_element_count
    )

    sequence = pr.PassSequence([
        roughing_train,
        intermediate_train,
        finishing_train_e107
    ])

    sequence.flatten()

    return sequence


def rolling_train_rpd3(roll_surface_temperature: float, disk_element_count: int):
    roughing_train = roughing_sequence(
        roll_surface_temperature=roll_surface_temperature,
        disk_element_count=disk_element_count
    )

    intermediate_train = intermediate_sequence(
        roll_surface_temperature=roll_surface_temperature,
        disk_element_count=disk_element_count
    )

    finishing_train_e107 = finishing_pass_design_3(
        roll_surface_temperature=roll_surface_temperature,
        disk_element_count=disk_element_count
    )

    sequence = pr.PassSequence([
        roughing_train,
        intermediate_train,
        finishing_train_e107
    ])

    sequence.flatten()

    return sequence