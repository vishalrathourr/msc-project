import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv 

def calculate_rayleigh_intensity(lambda_nm, I_0, r_um, n, d_cm):
    
    """
    **Note: Radius of particle r should not be greater than the wavelength of light λ**\n
    This function gives the data of Intensities wrt scattering angles in csv format as saves the file in current directory.\n
    Input the parameters in the following format -\n
    lambda_nm : Wavelength of light in nanometers
    r_um : Radius of the particle in micrometers
    n : Refractive index
    I_0 : Input intensity of light 
    d_cm : distance between scattering particle and observing point in cm
    """
    
    # Convert input parameters to SI units
    lambda_m = lambda_nm * 1e-9
    r = r_um * 1e-6
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
    intensity_perpendicular = np.full_like(theta_degrees, intensity_perpendicular)

    # Create a DataFrame to store the data
    data = pd.DataFrame({
        'Scattering Angle (degrees)': theta_degrees,
        'Intensity Parallel': intensity_parallel,
        'Intensity Perpendicular': intensity_perpendicular
    })

    # Save the data to a CSV file
    # data.to_csv('rayleigh_intensity_data.csv', index=False)
    print(data)

    return data

# Example usage:
lambda_nm = 650
r_um = 0.01
n = 1.33257
I_0 = 1
d_cm = 3
calculate_rayleigh_intensity(lambda_nm,I_0,r_um,n,d_cm)



