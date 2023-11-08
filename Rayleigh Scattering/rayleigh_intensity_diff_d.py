import numpy as np
import matplotlib.pyplot as plt

def plot_rayleigh_scattering_intensity(lambda_nm, I_0, r_um, n, d_cm_values):
    """
    This function plots the graph between scattering angle and Intensity for multiple observer distances.

    **Note: Radius of particle r should not be greater than the wavelength of light λ**
    
    Here Intensity is taken on the linear scale.
    
    Input the parameters in the following format -
    Args:
        lambda_nm : Wavelength of light in nanometers
        r_um : Radius of the particle in micrometers
        n : Refractive index
        I_0 : Input intensity of light
        d_cm_values : List of observer distances in cm.
    """
    # Convert input parameters to SI units
    lambda_m = lambda_nm * 1e-9
    r = r_um * 1e-6

    # Condition for Rayleigh scattering
    if r >= lambda_m:
        raise ValueError("Rayleigh scattering condition not satisfied.\n Radius of particle r should not be greater than the wavelength of light λ")

    # Scattering angles in degrees (from 0 to 180 degrees)
    theta_degrees = np.arange(0, 180.1, 0.1)

    # Convert scattering angles from degrees to radians
    theta_radians = np.deg2rad(theta_degrees)

    plt.figure(figsize=(10, 6))
    plt.style.use('seaborn-ticks')
    
    for d_cm in d_cm_values:
        d = d_cm * 1e-2

        # Calculate the Rayleigh scattering intensity for each scattering angle
        intensity_parallel = I_0 * (16 * np.pi**4 * r**6 / (lambda_m**4 * d**2)) * ((n**2 - 1) / (n**2 + 2))**2 * (np.cos(theta_radians))**2

        # Plot the graph for the current observer distance
        plt.plot(theta_degrees, intensity_parallel, label=f'd = {d_cm} cm')

    plt.xlabel('Scattering Angle (degrees)', color='black')
    plt.ylabel('Intensity', color='black')
    plt.xlim(0, 180)
    plt.xticks(np.arange(0, 181, 30))
    plt.tick_params(which='both', direction='in')
    plt.title('Rayleigh Scattering Intensity (Parallel) vs Scattering Angle', fontweight='bold', fontname='Franklin Gothic Medium')

    columnLabels = ['Input Parameters', 'Values']
    tableValues = [
        ['λ', f' {lambda_nm} nm'],
        ['Radius of particle(r)', f'{r_um} μm'],
        ['Ref. Index(n)', n],
        ['Incident Intensity $I_0$', f'{I_0} (W/m\u00B2)']
    ]
    my_table = plt.table(cellText=tableValues,
                        colWidths=[0.2, 0.1],
                        colLabels=columnLabels,
                        loc='upper center')

    plt.legend()
    plt.grid(False)
    plt.show()

# Example usage:
lambda_nm = 650  # Wavelength of light in nanometers
I_0 = 1       # Input intensity of light (W/m^2)
r_um = 0.01      # Radius of the particle in micrometers
n = 1.33257      # Refractive index
# d_cm_values = [4.8, 4.9, 5.0, 5.1, 5.2]  # List of observer distances in cm
d_cm_values = [1, 2, 3, 4, 5]  # List of observer distances in cm


plot_rayleigh_scattering_intensity(lambda_nm, I_0, r_um, n, d_cm_values)
