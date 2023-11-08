import numpy as np
import matplotlib.pyplot as plt

def plot_rayleigh_scattering(lambda_nm, r_um, n):
    """
    **Note: Radius of particle r should not be greater than the wavelength of light λ**
    This function plots the graph between the scattering angle and square of Amplitude.\n
    Input the parameters in the following format -\n
    Args:
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
    S1 = np.full_like(theta_degrees, S1)
    S2 = (2 * np.pi * r / lambda_m)**2 * (n**2 - 1) / (n**2 + 2) * np.cos(theta_radians)

    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Rayleigh Scattering', fontsize=16)

    # Plot the linear scale intensity in the first subplot
    axs[0].plot(theta_degrees, S1**2, color='red', label='S1: Perpendicular Polarization', linestyle='--')
    axs[0].plot(theta_degrees, S2**2, color='red', label='S2: Parallel Polarization')
    axs[0].set_xlabel('Scattering Angle (degrees)')
    axs[0].set_ylabel('$|S(θ)|^2$')
    axs[0].set_xlim(0, 180)
    axs[0].set_xticks(np.arange(0, 181, 30))
    axs[0].tick_params(which='both', direction='in')
    axs[0].set_title('Linear Scale', fontweight='bold')
    axs[0].legend(loc='lower left',frameon=False, prop={'size': 8})
    axs[0].grid(False)

    # Plot the log scale intensity in the second subplot
    axs[1].semilogy(theta_degrees, S1**2, color='red', label='S1: Perpendicular Polarization', linestyle='--')
    axs[1].semilogy(theta_degrees, S2**2, color='red', label='S2: Parallel Polarization')
    axs[1].set_xlabel('Scattering Angle (degrees)')
    axs[1].set_ylabel('$|S(θ)|^2$')
    axs[1].set_xlim(0, 180)
    axs[1].set_xticks(np.arange(0, 181, 30))
    axs[1].tick_params(which='both', direction='in')
    axs[1].set_title('Log Scale', fontweight='bold')
    axs[1].legend(loc='lower left',frameon=False, prop={'size': 8})
    axs[1].grid(False)
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    columnLabels = ['Input Parameters', 'Values']
    tableValues = [['λ', f' {lambda_nm} nm'], ['Radius of particle(r)', f'{r_um} μm'], ['Ref. Index(n)', n], ]
    my_table = axs[1].table(cellText=tableValues,
                            colWidths=[0.25, 0.15],
                            colLabels=columnLabels,
                            loc='lower right',
                            fontsize=10)
    plt.show()

# Example usage:
lambda_nm = 650
r_um = 0.01
n = 1.33257
plot_rayleigh_scattering(lambda_nm, r_um, n)

