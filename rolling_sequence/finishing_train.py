import pyroll.core as pr

# E11.2
def finishing_pass_design_1(roll_surface_temperature: float = 50 + 273.15, disk_element_count: int = 30):
    ROLL_SURFACE_TEMPERATURE = roll_surface_temperature
    DISK_ELEMENT_COUNT = disk_element_count

    return pr.PassSequence([
        pr.RollPass(
            label="17-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=7.4e-3,
                    r1=1e-3,
                    r2=23e-3,
                ),
                nominal_radius=104e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=17.1,
            gap=2.3e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="17 => 18",
            length=0.85
        ),
        pr.RollPass(
            label="18-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=8.7e-3,
                    r1=0.2e-3,
                    r2=10.3e-3,
                    flank_angle=60
                ),
                nominal_radius=104e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=22.2,
            gap=2.1e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            disk_element_count=30,
            label="18 => 21",
            length=17.2,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP I",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP II",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP III",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP IV",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP V",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP VI",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP VII",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP VIII",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP IX",
            length=0.65,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - Stand 21",
            length=12.4,
        ),
        pr.RollPass(
            label="21-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=4.5e-3,
                    r1=1e-3,
                    r2=20e-3,
                ),
                nominal_radius=95.17e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=30,
            gap=2.7e-3,
            sparling_material_coefficient=0.75,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="21 => 22",
            length=0.85
        ),
        pr.RollPass(
            label="22-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=6.6e-3,
                    r1=0.2e-3,
                    r2=7e-3,
                    flank_angle=60
                ),
                nominal_radius=95.17e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=37.8,
            gap=2.2e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="22 => 23",
            length=0.85
        ),
        pr.RollPass(
            label="23-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=3.5e-3,
                    r1=1e-3,
                    r2=15.5e-3
                ),
                nominal_radius=72.75e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=51,
            gap=2.4e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="23 => 24",
            length=0.85
        ),
        pr.RollPass(
            label="24-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=4.85e-3,
                    r1=0.2e-3,
                    r2=5.85e-3,
                    flank_angle=70
                ),
                nominal_radius=72.75e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=65.4,
            gap=1.7e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            disk_element_count=30,
            label="24 => 27",
            length=4.7,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP I",
            length=0.65
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP II",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP III",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP IV",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP V",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP VI",
            length=0.65
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP VII",
            length=0.65
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP VIII",
            length=0.65
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP IX",
            length=0.65,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - Stand 27",
            length=6.4,
        ),
        pr.RollPass(
            label="27-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=2.4e-3,
                    r1=1e-3,
                    r2=14e-3
                ),
                nominal_radius=106e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=81.7,
            gap=1.7e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="27 => 28",
            length=0.75
        ),

        pr.RollPass(
            label="28-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=3.5e-3,
                    r1=0.2e-3,
                    r2=4.33e-3,
                    flank_angle=75
                ),
                nominal_radius=106e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=107,
            gap=1.7e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        )
])

# E10.7
def finishing_pass_design_2(roll_surface_temperature: float = 50 + 273.15, disk_element_count: int = 30):
    ROLL_SURFACE_TEMPERATURE = roll_surface_temperature
    DISK_ELEMENT_COUNT = disk_element_count

    return pr.PassSequence([
        pr.RollPass(
            label="17-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=5.7e-3,
                    r1=1e-3,
                    r2=23e-3,
                ),
                nominal_radius=104e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=17.1,
            gap=3.8e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="17 => 18",
            length=0.85
        ),
        pr.RollPass(
            label="18-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=8e-3,
                    r1=0.2e-3,
                    r2=8.5e-3,
                    flank_angle=60
                ),
                nominal_radius=104e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=22.2,
            gap=2.8e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            disk_element_count=30,
            label="18 => 21",
            length=17.2,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP I",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP II",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP III",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP IV",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP V",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP VI",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP VII",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP VIII",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP IX",
            length=0.65,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - Stand 21",
            length=12.4,
        ),
        pr.RollPass(
            label="21-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=4.5e-3,
                    r1=1e-3,
                    r2=20e-3,
                ),
                nominal_radius=95.17e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=30,
            gap=2.3e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="21 => 22",
            length=0.85
        ),
        pr.RollPass(
            label="22-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=6.6e-3,
                    r1=0.2e-3,
                    r2=7e-3,
                    flank_angle=60
                ),
                nominal_radius=95.17e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=37.8,
            gap=1.2e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="22 => 23",
            length=0.85
        ),
        pr.RollPass(
            label="23-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=3.5e-3,
                    r1=1e-3,
                    r2=15.5e-3
                ),
                nominal_radius=72.75e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=51,
            gap=1.5e-3,
            sparling_material_coefficient=0.7,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="23 => 24",
            length=0.85
        ),
        pr.RollPass(
            label="24-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=4.6e-3,
                    r1=0.2e-3,
                    r2=5.45e-3,
                    flank_angle=70
                ),
                nominal_radius=72.75e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=65.4,
            gap=1.6e-3,
            sparling_material_coefficient=0.7,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            disk_element_count=30,
            label="24 => 27",
            length=4.7,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP I",
            length=0.65
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP II",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP III",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP IV",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP V",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP VI",
            length=0.65
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP VII",
            length=0.65
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP VIII",
            length=0.65
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP IX",
            length=0.65,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - Stand 27",
            length=6.4,
        ),
        pr.RollPass(
            label="27-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=2.4e-3,
                    r1=1e-3,
                    r2=14e-3
                ),
                nominal_radius=106e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=81.7,
            gap=1.7e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="27 => 28",
            length=0.75
        ),

        pr.RollPass(
            label="28-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=3.5e-3,
                    r1=0.2e-3,
                    r2=4.33e-3,
                    flank_angle=75
                ),
                nominal_radius=106e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=107,
            gap=1.7e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        )
])

# E10.7 - 2
def finishing_pass_design_3(roll_surface_temperature: float = 50 + 273.15, disk_element_count: int = 30):
    ROLL_SURFACE_TEMPERATURE = roll_surface_temperature
    DISK_ELEMENT_COUNT = disk_element_count

    return pr.PassSequence([
        pr.RollPass(
            label="17-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=6.5e-3,
                    r1=1e-3,
                    r2=24.5e-3,
                ),
                nominal_radius=104e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=17.1,
            gap=2.6e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="17 => 18",
            length=0.85
        ),
        pr.RollPass(
            label="18-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=8.2e-3,
                    r1=1e-3,
                    r2=9.53e-3,
                    flank_angle=60
                ),
                nominal_radius=104e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=22.2,
            gap=2.6e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            disk_element_count=30,
            label="18 => 21",
            length=17.2,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP I",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP II",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP III",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP IV",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP V",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP VI",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP VII",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP VIII",
            length=0.65,
            inner_radius=12.5e-3,
            coolant_volume_flux=0.005659725,
            coolant_temperature=40 + 273.15,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP IX",
            length=0.65,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - Stand 21",
            length=12.4,
        ),
        pr.RollPass(
            label="21-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=4.5e-3,
                    r1=1e-3,
                    r2=20e-3,
                ),
                nominal_radius=95.17e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=30,
            gap=2.3e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="21 => 22",
            length=0.85
        ),
        pr.RollPass(
            label="22-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=6.6e-3,
                    r1=0.2e-3,
                    r2=7e-3,
                    flank_angle=60
                ),
                nominal_radius=95.17e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=37.8,
            gap=2.2e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="22 => 23",
            length=0.85
        ),
        pr.RollPass(
            label="23-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=3.5e-3,
                    r1=1e-3,
                    r2=15.5e-3
                ),
                nominal_radius=72.75e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=51,
            gap=1.9e-3,
            sparling_material_coefficient=0.7,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="23 => 24",
            length=0.85
        ),
        pr.RollPass(
            label="24-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=4.6e-3,
                    r1=0.2e-3,
                    r2=5.45e-3,
                    flank_angle=70
                ),
                nominal_radius=72.75e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=65.4,
            gap=1.7e-3,
            sparling_material_coefficient=0.7,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            disk_element_count=30,
            label="24 => 27",
            length=4.7,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP I",
            length=0.65
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP II",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP III",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP IV",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.CoolingPipe(
            disk_element_count=30,
            label="PreCooler - CP V",
            length=0.65,
            inner_radius=9e-3,
            coolant_volume_flux=0.00465278,
            coolant_temperature=40 + 273.15,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP VI",
            length=0.65
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP VII",
            length=0.65
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP VIII",
            length=0.65
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - CP IX",
            length=0.65,
        ),
        pr.Transport(
            disk_element_count=30,
            label="PreCooler - Stand 27",
            length=6.4,
        ),
        pr.RollPass(
            label="27-H",
            orientation="h",
            roll=pr.Roll(
                groove=pr.CircularOvalGroove(
                    depth=2.4e-3,
                    r1=1e-3,
                    r2=14e-3
                ),
                nominal_radius=106e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=81.7,
            gap=1.7e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        ),
        pr.Transport(
            label="27 => 28",
            length=0.75
        ),

        pr.RollPass(
            label="28-V",
            orientation="v",
            roll=pr.Roll(
                groove=pr.FalseRoundGroove(
                    depth=3.5e-3,
                    r1=0.2e-3,
                    r2=4.33e-3,
                    flank_angle=75
                ),
                nominal_radius=106e-3,
                temperature=ROLL_SURFACE_TEMPERATURE
            ),
            velocity=107,
            gap=1.7e-3,
            sparling_material_coefficient=0.8,
            disk_element_count=DISK_ELEMENT_COUNT
        )
])