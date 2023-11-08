import numpy as np
import pandas as pd

def calculate_rayleigh_intensity(lambda_nm, I_0, r_um, n, d_range):
    # Create an Excel writer
    writer = pd.ExcelWriter('rayleigh_intensity_data.xlsx', engine='xlsxwriter')

    # Convert input parameters to SI units
    lambda_m = lambda_nm * 1e-9
    r = r_um * 1e-6

    for d_cm in d_range:
        d = d_cm * 1e-2

        # Condition for Rayleigh scattering
        if r >= lambda_m:
            raise ValueError("Rayleigh scattering condition not satisfied.\nRadius of particle r should not be greater than the wavelength of light λ")

        # Scattering angles in degrees (from 0 to 180 degrees)
        theta_degrees = np.arange(0, 180.1, 0.1)

        # Convert scattering angles from degrees to radians
        theta_radians = np.deg2rad(theta_degrees)

        # Calculate the Rayleigh scattering intensity for each scattering angle
        intensity_parallel = I_0 * (16 * np.pi**4 * r**6 / (lambda_m**4 * d**2)) * ((n**2 - 1) / (n**2 + 2))**2 * (np.cos(theta_radians))**2
        intensity_perpendicular = I_0 * (16 * np.pi**4 * r**6 / (lambda_m**4 * d**2)) * ((n**2 - 1) / (n**2 + 2))**2

        # Create a DataFrame for the current d_cm value
        data = pd.DataFrame({
            'Scattering Angle (degrees)': theta_degrees,
            'Intensity Perpendicular': intensity_perpendicular,
            'Intensity Parallel': intensity_parallel
        })

        # Write the DataFrame to a new sheet in the Excel file
        data.to_excel(writer, sheet_name=f'd_cm_{d_cm:.1f}', index=False)

    # Save the Excel file
    writer._save()

# Example usage:
lambda_nm = 650
r_um = 0.01
n = 1.33257
I_0 = 1
d_range = np.arange(2.1, 5.1,0.1)  # Range of d_cm values

calculate_rayleigh_intensity(lambda_nm, I_0, r_um, n, d_range)
