import numpy as np
import matplotlib.pyplot as plt

def plot_rayleigh_scattering_intensity(lambda_nm, I_0, r_um, n, d_cm):
    """
    This function plots the graph between scattering angle and Intensity .\n
    **Note: Radius of particle r should not be greater than the wavelength of light λ**\n
    Input the parameters in the following format -\n
    Args:
        lambda_nm : Wavelength of light in nanometers
        r_um : Radius of the particle in micrometers
        n : Refractive index
        I_0 : Input intensity of light 
        d_cm : distance between scattering particle and observing point in cm.
    """
    # Convert input parameters to SI units
    lambda_m = lambda_nm * 1e-9
    r = r_um * 1e-6
    d = d_cm * 1e-2

    # Condition for Rayleigh scattering
    if r >= lambda_m:
        raise ValueError("Rayleigh scattering condition not satisfied.\n Radius of particle r should not be greater than the wavelength of light λ")

    # Scattering angles in degrees (from 0 to 180 degrees)
    theta_degrees = np.linspace(0, 180, 1000)

    # Convert scattering angles from degrees to radians
    theta_radians = np.deg2rad(theta_degrees)

    # Calculate the Rayleigh scattering intensity for each scattering angle
    intensity_parallel = I_0 * (16 * np.pi**4 * r**6 / (lambda_m**4 * d**2)) * ((n**2 - 1) / (n**2 + 2))**2 * (np.cos(theta_radians))**2
    intensity_perpendicular = I_0 * (16 * np.pi**4 * r**6 / (lambda_m**4 * d**2)) * ((n**2 - 1) / (n**2 + 2))**2
    intensity_perpendicular = np.full_like(theta_degrees, intensity_perpendicular)

    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Rayleigh Scattering Intensity vs Scattering Angle', fontsize=16)

    # Plot the linear scale intensity in the first subplot
    axs[0].plot(theta_degrees, intensity_parallel, color='red', label='Parallel Polarization')
    axs[0].plot(theta_degrees, intensity_perpendicular, color='red', linestyle='--', label='Perpendicular Polarization')
    axs[0].set_xlabel('Scattering Angle (degrees)')
    axs[0].set_ylabel('Intensity')
    axs[0].set_xlim(0, 180)
    axs[0].set_xticks(np.arange(0, 181, 30))
    axs[0].tick_params(which='both', direction='in')
    axs[0].set_title('Linear Scale', fontweight='bold')
    axs[0].legend(loc='lower left',frameon=False, prop={'size': 8})
    axs[0].grid(False)

    # Plot the log scale intensity in the second subplot
    axs[1].plot(theta_degrees, intensity_parallel, color='r', label='Parallel Polarization')
    axs[1].plot(theta_degrees, intensity_perpendicular, color='r', linestyle='--', label='Perpendicular Polarization')
    axs[1].set_xlabel('Scattering Angle (degrees)')
    axs[1].set_ylabel('Intensity (log scale)')
    axs[1].set_yscale('log')  # Set the y-axis to log scale
    axs[1].set_xlim(0, 180)
    axs[1].set_xticks(np.arange(0, 181, 30))
    axs[1].tick_params(which='both', direction='in')
    axs[1].set_title('Log Scale', fontweight='bold')
    axs[1].legend(loc='lower left',frameon=False, prop={'size': 8})
    axs[1].grid(False)

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # columnLabels = ['Input Parameters', 'Values']
    tableValues = [
        ['λ', f' {lambda_nm} nm'],
        ['Radius of particle(r)', f'{r_um} μm'],
        ['Ref. Index(n)', n],
        ['Observer Distance', f'{d_cm} cm'],
        ['Incident Intensity $I_0$', f'{I_0} (W/m\u00B2)']
    ]
    my_table = axs[1].table(cellText=tableValues,
                            colWidths=[0.25, 0.15],
                            # colLabels=columnLabels,
                            loc='lower right')

    plt.show()

# Example usage:
lambda_nm = 650
r_um = 0.01
n = 1.33257
I_0 = 1
d_cm = 4

plot_rayleigh_scattering_intensity(lambda_nm, I_0, r_um, n, d_cm)
