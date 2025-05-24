import pyroll.core as pr


def intermediate_sequence(roll_surface_temperature: float = 50 + + 273.15, disk_element_count: int = 30):
    ROLL_SURFACE_TEMPERATURE = roll_surface_temperature
    DISK_ELEMENT_COUNT = disk_element_count

    return pr.PassSequence([
        pr.Transport(
        label="6 => 7",
        length=5.5
        ),
        pr.RollPass(
            label="7",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=17.5e-3,
                    r1=7e-3,
                    r2=60e-3
                ),
                nominal_radius=450e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=2.55,
            gap=7e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        ),
        pr.Transport(
            label="7 => 8",
            length=4.2,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="8",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=22.75e-3,
                    r1=4.5e-3,
                    r2=25.75e-3,
                    flank_angle=65
                ),
                nominal_radius=450e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=3.05,
            gap=6e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        ),
        pr.Transport(
            label="8 => 9",
            length=4.2,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="9",
            orientation="h",
            roll=pr.Roll(
                groove=pr.Oval3RadiiGroove(
                    depth=12e-3,
                    r1=5e-3,
                    r2=8.8e-3,
                    r3=71e-3,
                    usable_width=69.03e-3
                ),
                nominal_radius=450e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=4.15,
            gap=5e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        ),
        pr.Transport(
            label="9 => 10",
            length=4.2,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="10",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=17.25e-3,
                    r1=3.5e-3,
                    r2=19.25e-3,
                    flank_angle=59.99
                ),
                nominal_radius=450e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=5.33,
            gap=4e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        ),
        pr.Transport(
            label="10 => 11",
            length=4.2,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="11",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=9.5e-3,
                    r1=5e-3,
                    r2=40e-3
                ),
                nominal_radius=177e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=6.87,
            gap=4.5e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        ),
        pr.Transport(
            label="11 => 12",
            length=2.5,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="12",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=13e-3,
                    r1=2.5e-3,
                    r2=14.9e-3,
                    flank_angle=60
                ),
                nominal_radius=169e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=8.44,
            gap=4.4e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        ),
        pr.Transport(
            label="12 => 13",
            length=2.5,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="13",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=7.5e-3,
                    r1=4e-3,
                    r2=31e-3,
                ),
                nominal_radius=163e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=10.8,
            gap=3.4e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        ),
        pr.Transport(
            label="13 => 14",
            length=2.5,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="14",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=10.25e-3,
                    r1=2.5e-3,
                    r2=12e-3,
                    flank_angle=60
                ),
                nominal_radius=179e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=13,
            gap=3.5e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        )
    ])
