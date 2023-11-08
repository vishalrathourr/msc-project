import numpy as np
import pandas as pd

def rayleigh_scattering_data(lambda_nm, r_um, n):
    
    """
    This function gives the data of S1 and S2 wrt scattering angles in csv format as saves the file in current directory.\n
    **Note: Radius of particle r should not be greater than the wavelength of light λ**\n
    Input the parameters in the following format -\n
    lambda_nm : Wavelength of light in nanometers
    r_um : Radius of the particle in micrometers
    n : Refractive index 
    """
    # Convert input parameters to SI units
    lambda_m = lambda_nm * 1e-9
    r = r_um * 1e-6

    # Condition for Rayleigh scattering
    if r >= lambda_m:
        raise ValueError("Rayleigh scattering condition not satisfied.\n Radius of particle r should not be greater than the wavelength of light λ")

    # Scattering angles in degrees (from 0 to 180 degrees)
    theta_degrees = np.linspace(0, 180, 1000)

    # Convert scattering angles from degrees to radians
    theta_radians = np.deg2rad(theta_degrees)

    # Calculate the S1 and S2 values for each scattering angle
    S1 = (2 * np.pi * r / lambda_m)**2 * (n**2 - 1) / (n**2 + 2)
    S2 = (2 * np.pi * r / lambda_m)**2 * (n**2 - 1) / (n**2 + 2) * np.cos(theta_radians)

    # Create a DataFrame to store the data
    data = pd.DataFrame({
        'Scattering Angle (degrees)': theta_degrees,
        'S1': S1,
        'S2': S2
    })

    # Save the data to a CSV file
    data.to_csv('rayleigh_scattering_data.csv', index=False)

# Example usage:
lambda_nm = 650
r_um = 0.01
n = 1.33257
rayleigh_scattering_data(lambda_nm, r_um, n)
