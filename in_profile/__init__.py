import pathlib
import pandas as pd
import pyroll.core as pr
from scipy.interpolate import interp1d

filepath = pathlib.Path.cwd()

density = pd.read_csv(filepath / "in_profile" / "bst500_density.csv").density
density_temperature = pd.read_csv(filepath / "in_profile" / "bst500_density.csv").kelvin_temperature
specific_heat_capacity_real = pd.read_csv(filepath / "in_profile" / "bst500_specific_heat_capacity_real_measurement.csv").specific_heat_capacity * 1000
specific_heat_capacity_temperature_real = pd.read_csv(filepath / "in_profile" / "bst500_specific_heat_capacity_real_measurement.csv").celsius_temperature + 273.15
specific_heat_capacity = pd.read_csv(filepath / "in_profile" / "bst500_specific_heat_capacity.csv").specific_heat_capacity * 1000
specific_heat_capacity_temperature = pd.read_csv(filepath / "in_profile" / "bst500_specific_heat_capacity.csv").celsius_temperature + 273.15
thermal_conductivity = pd.read_csv(filepath / "in_profile" / "bst500_thermal_conductivity.csv").thermal_conductivity
thermal_conductivity_temperature = pd.read_csv(filepath / "in_profile" / "bst500_thermal_conductivity.csv").celsius_temperature + 273.15

density_function = interp1d(density_temperature, density)
specific_heat_capacity_function = interp1d(specific_heat_capacity_temperature, specific_heat_capacity)
thermal_conductivity_function = interp1d(thermal_conductivity_temperature, thermal_conductivity)


@pr.Profile.density
def density(self: pr.Profile):
    return density_function(self.temperature)


@pr.Profile.specific_heat_capacity
def specific_heat_capacity(self: pr.Profile):
    return specific_heat_capacity_function(self.temperature)


@pr.Profile.thermal_conductivity
def thermal_conductivity(self: pr.Profile):
    return thermal_conductivity_function(self.temperature)


def create_in_profile_from_surface_temperature(temperature: float) -> pr.Profile:
    in_profile = pr.Profile.box(
        height=160e-3,
        width=160e-3,
        corner_radius=3e-3,
        temperature=temperature,
        strain=0,
        flow_stress=100e6,
        weight=2400,
        length=12,
        material=["BST500", "steel"]
    )
    return in_profile