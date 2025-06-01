import pyroll.core as pr


def roughing_sequence(roll_surface_temperature: float = 50 + + 273.15, disk_element_count: int = 30):
    ROLL_SURFACE_TEMPERATURE = roll_surface_temperature
    DISK_ELEMENT_COUNT = disk_element_count

    return pr.PassSequence([
        pr.RollPass(
            label="A",
            orientation="h",
            roll=pr.Roll(
                groove=pr.BoxGroove(
                    usable_width=183.97e-3,
                    depth=48e-3,
                    ground_width=157.72e-3,
                    r1=15e-3,
                    r2=18e-3
                ),
                nominal_radius=635e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=0.315,
            gap=20e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        ),
        pr.Transport(
            label="A => B",
            length=2.5,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="B",
            orientation="v",
            roll=pr.Roll(
                groove=pr.BoxGroove(
                    usable_width=137.096e-3,
                    depth=53e-3,
                    ground_width=108.693e-3,
                    r1=15e-3,
                    r2=20e-3
                ),
                nominal_radius=635e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE,
            ),
            gap=20e-3,
            velocity=0.409,
            sparling_material_coefficient=1,
            disk_element_count=DISK_ELEMENT_COUNT,
            coulomb_friction_coefficient=0.4
        ),
        pr.Transport(
            label="B => 1",
            length=2.5,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="1",
            orientation="h",
            roll=pr.Roll(
                groove=pr.Oval3RadiiFlankedGroove(
                    depth=36.4e-3,
                    r1=6e-3,
                    r2=23.5e-3,
                    r3=183e-3,
                    flank_angle=70.3,
                    usable_width=145.03e-3
                ),
                nominal_radius=635e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE,
            ),
            velocity=0.55,
            gap=15e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="1 => 2",
            length=2.5,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="2",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=44.5e-3,
                    r1=8e-3,
                    r2=52e-3,
                    flank_angle=65
                ),
                nominal_radius=635e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE,
            ),
            velocity=0.709,
            gap=15e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="2 => 3",
            length=2.5,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="3",
            orientation="h",
            roll=pr.Roll(
                groove=pr.Oval3RadiiGroove(
                    depth=24.3e-3,
                    r1=6e-3,
                    r2=30e-3,
                    r3=170e-3,
                    usable_width=124.618e-3
                ),
                nominal_radius=530e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=0.994,
            gap=15e-3,
            sparling_material_coefficient=1,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="3 => 4",
            length=2.4,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="4",
            orientation="v",
            roll=pr.Roll(
                groove=pr.RoundGroove(
                    depth=34.5e-3,
                    r1=6e-3,
                    r2=39.5e-3
                ),
                nominal_radius=530e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=1.2,
            gap=10e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="4 => 5",
            length=2.4,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="5",
            orientation="h",
            roll=pr.Roll(
                groove=pr.Oval3RadiiGroove(
                    depth=21.9e-3,
                    r1=6e-3,
                    r2=34e-3,
                    r3=81.5e-3,
                    usable_width=91.32e-3
                ),
                nominal_radius=530e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=1.55,
            gap=10e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="5 => 6",
            length=2.4,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.RollPass(
            label="6",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=27e-3,
                    r1=6e-3,
                    r2=32e-3,
                    flank_angle=65
                ),
                nominal_radius=530e-3 / 2,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=1.99,
            gap=10e-3,
            sparling_material_coefficient=0.9,
            disk_element_count=DISK_ELEMENT_COUNT
        )
    ])
