import PyMieScatt as ps
import numpy as np
import matplotlib.pyplot as plt

m = 1.33257 + 1.67E-08j  # Refractive index
w = 650  # Wavelength in nanometers
r = 1000  # Radius in nanometers
d = 2 * r

theta, SL, SR, SU = ps.ScatteringFunction(m, w, d)
theta_deg = theta * (180 / np.pi)

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Subplot 1: SR vs theta_deg
axs[0, 0].semilogy(theta_deg, SR, 'r--', lw=1, label='Parallel')
# axs[0, 0].set_title("Mie scattering parallel polarization")
# axs[0, 0].set_xlabel("Scattering angle (θ) [degrees]")
axs[0, 0].set_ylabel("Intensity ($|S_R|^2$)")
axs[0, 0].legend()
axs[0, 0].set_xlim(0, 180)
axs[0, 0].set_xticks(np.arange(0, 181, 30))

# Subplot 2: SL vs theta_deg
axs[0, 1].semilogy(theta_deg, SL, 'r', lw=1, label='Perpendicular')
# axs[0, 1].set_title("Mie scattering perpendicular polarization")
# axs[0, 1].set_xlabel("Scattering angle (θ) [degrees]")
axs[0, 1].set_ylabel("Intensity ($|S_L|^2$)")
axs[0, 1].set_xlim(0, 180)
axs[0, 1].legend()
axs[0, 1].set_xticks(np.arange(0, 181, 30))

# Subplot 3: SU vs theta_deg
axs[1, 0].semilogy(theta_deg, SU, 'b', lw=1, label = 'Unpolarized')
# axs[1, 0].set_title("Mie scattering Unpolarized light")
axs[1, 0].set_xlabel("Scattering angle (θ) [degrees]")
axs[1, 0].set_ylabel("Intensity ($|S_U|^2$)")
axs[1, 0].legend()
axs[1, 0].set_xlim(0, 180)
axs[1, 0].set_xticks(np.arange(0, 181, 30))

# Subplot 4: SL, SR, SU vs theta_deg
axs[1, 1].semilogy(theta_deg, SR, 'r--', lw=1, label="Parallel")
axs[1, 1].semilogy(theta_deg, SL, 'r', lw=1, label="Perpendicular")
axs[1, 1].semilogy(theta_deg, SU, 'b', lw=1, label="Unpolarized")
# axs[1, 1].set_title("SL, SR, SU vs Scattering Angle")
axs[1, 1].set_xlabel("Scattering angle (θ) [degrees]")
axs[1, 1].set_ylabel("Intensity")
axs[1, 1].legend()
axs[1, 1].set_xlim(0, 180)
axs[1, 1].set_xticks(np.arange(0, 181, 30))

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
