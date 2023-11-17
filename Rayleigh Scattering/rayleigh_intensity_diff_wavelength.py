import numpy as np
import matplotlib.pyplot as plt

def plot_rayleigh_scattering_intensity(lambda_nm, I_0, r_um, n, d_cm, ax_linear=None, ax_log=None, label=None):
    """
    This function plots the graph between scattering angle and Intensity.
    **Note: Radius of particle r should not be greater than the wavelength of light λ**
    Input the parameters in the following format -
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

    # Plot the Rayleigh scattering intensity for the given wavelength on linear scale
    if ax_linear is not None:
        ax_linear.plot(theta_degrees, intensity_parallel, label=f'λ = {lambda_nm} nm' if label is None else label)

    # Plot the Rayleigh scattering intensity for the given wavelength on log scale
    if ax_log is not None:
        ax_log.plot(theta_degrees, intensity_parallel, label=f'λ = {lambda_nm} nm' if label is None else label)

    return ax_linear, ax_log

# Example usage:
wavelengths = [532, 650, 800]
r_um = 0.01
n = 1.33257
I_0 = 1
d_cm = 4

# Create subplots for linear and log scale
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Plot for linear scale
axs[0].set_xlabel('Scattering Angle (degrees)')
axs[0].set_ylabel('Intensity')
axs[0].set_xlim(0, 180)
axs[0].set_xticks(np.arange(0, 181, 30))
axs[0].tick_params(which='both', direction='in')
axs[0].set_title('Linear Scale', fontweight='bold')

# Plot for log scale
axs[1].set_xlabel('Scattering Angle (degrees)')
axs[1].set_ylabel('Intensity (log scale)')
axs[1].set_yscale('log')  # Set the y-axis to log scale
axs[1].set_xlim(0, 180)
axs[1].set_xticks(np.arange(0, 181, 30))
axs[1].tick_params(which='both', direction='in')
axs[1].set_title('Log Scale', fontweight='bold')
# Display input parameters in a table
tableValues = [
        ['Radius of particle(r)', f'{r_um} μm'],
        ['Ref. Index(n)', n],
        ['Observer Distance', f'{d_cm} cm'],
        ['Incident Intensity $I_0$', f'{I_0} (W/m\u00B2)']
    ]
my_table = axs[1].table(cellText=tableValues,
                            colWidths=[0.25, 0.15],
                            loc='lower right')

# Iterate over wavelengths and plot on both linear and log scales
for wavelength in wavelengths:
    plot_rayleigh_scattering_intensity(wavelength, I_0, r_um, n, d_cm, ax_linear=axs[0], ax_log=axs[1])

# Add legends
axs[0].legend(frameon=False)
axs[1].legend(frameon=False)

plt.tight_layout()
plt.show()
