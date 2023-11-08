import numpy as np
import matplotlib.pyplot as plt

def plot_rayleigh_scattering_intensity(lambda_nm, I_0, d_cm, n, r_um_values):
    """
    This function plots the graph between scattering angle and Intensity for multiple particle radii.
    **Note: Radius of particle r should not be greater than the wavelength of light λ**
    Input the parameters in the following format -
    lambda_nm : Wavelength of light in nanometers
    d_cm : Observer distance in cm.
    n : Refractive index
    I_0 : Input intensity of light
    r_um_values : List of particle radii in micrometers.
    """
    # Convert input parameters to SI units
    lambda_m = lambda_nm * 1e-9
    d = d_cm * 1e-2

    # Scattering angles in degrees (from 0 to 180 degrees)
    theta_degrees = np.arange(0, 180.1, 0.1)

    # Convert scattering angles from degrees to radians
    theta_radians = np.deg2rad(theta_degrees)

    plt.figure(figsize=(14, 6))  # Increase figure width to accommodate two subplots

    # Plot the linear y-scale graph on the left side
    plt.subplot(1, 2, 1)
    plt.style.use('seaborn-ticks')

    for r_um in r_um_values:
        r = r_um * 1e-6

        # Condition for Rayleigh scattering
        if r >= lambda_m:
            raise ValueError("Rayleigh scattering condition not satisfied.\n Radius of particle r should not be greater than the wavelength of light λ")

        # Calculate the Rayleigh scattering intensity for each scattering angle
        intensity_parallel = I_0 * (16 * np.pi**4 * r**6 / (lambda_m**4 * d**2)) * ((n**2 - 1) / (n**2 + 2))**2 * (np.cos(theta_radians))**2

        # Plot the graph for the current particle radius
        plt.plot(theta_degrees, intensity_parallel, label=f'r = {r_um} μm')

    plt.xlabel('Scattering Angle (degrees)', color='black')
    plt.ylabel('Intensity', color='black')
    plt.xlim(0, 180)
    plt.xticks(np.arange(0, 181, 30))
    plt.tick_params(which='both', direction='in')
    plt.legend()
    plt.title('Linear Scale', fontweight='bold', fontname='Franklin Gothic Medium')

    # Plot the log y-scale graph on the right side
    plt.subplot(1, 2, 2)
    for r_um in r_um_values:
        r = r_um * 1e-6

        # Condition for Rayleigh scattering
        if r >= lambda_m:
            raise ValueError("Rayleigh scattering condition not satisfied.\n Radius of particle r should not be greater than the wavelength of light λ")

        # Calculate the Rayleigh scattering intensity for each scattering angle
        intensity_parallel = I_0 * (16 * np.pi**4 * r**6 / (lambda_m**4 * d**2)) * ((n**2 - 1) / (n**2 + 2))**2 * (np.cos(theta_radians))**2

        # Plot the graph for the current particle radius
        plt.plot(theta_degrees, intensity_parallel, label=f'r = {r_um} μm')

    plt.xlabel('Scattering Angle (degrees)', color='black')
    plt.yscale('log')
    plt.xlim(0, 180)
    plt.xticks(np.arange(0, 181, 30))
    plt.tick_params(which='both', direction='in')
    plt.title('Log Scale', fontweight='bold', fontname='Franklin Gothic Medium')

    # Create the table in the second subplot
    columnLabels = ['Input Parameters', 'Values']
    tableValues = [
        ['λ', f' {lambda_nm} nm'],
        ['Observer Distance(d)', f'{d_cm} cm'],
        ['Ref. Index(n)', n],
        ['Incident Intensity $I_0$', f'{I_0} (W/m\u00B2)']
    ]
    my_table = plt.table(cellText=tableValues,
                        colWidths=[0.25, 0.15],
                        colLabels=columnLabels,
                        loc='lower right',
                        fontsize=10)

    plt.legend()
    plt.grid(False)

    plt.tight_layout()  # Adjust the layout to prevent overlap
    plt.show()

# Example usage:
lambda_nm = 650  # Wavelength of light in nanometers
I_0 = 1         # Input intensity of light (W/m^2)
d_cm = 4        # Observer distance in cm
n = 1.33257      # Refractive index
r_um_values = [0.0001,0.001, 0.01, 0.1]  # List of particle radii in micrometers

plot_rayleigh_scattering_intensity(lambda_nm, I_0, d_cm, n, r_um_values)
