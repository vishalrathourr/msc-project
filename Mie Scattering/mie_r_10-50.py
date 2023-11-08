import PyMieScatt as ps
import numpy as np
import matplotlib.pyplot as plt

m = 1.33257 + 1.67E-08j    # Refractive index
w = 800                    # Wavelength in nanometers
radii = [10, 20, 25, 30, 40, 50]  # List of radii in nanometers
theta_deg = np.linspace(0, 180, 100)

plt.figure(figsize=(10, 6))

# Iterate over different radii and plot their scattering intensity functions for both polarizations
for r in radii:
    d = 2 * r * 1000
    theta, SL, SR, SU = ps.ScatteringFunction(m, w, d)
    theta_deg = theta * (180 / np.pi)
    label = f"Radius {r} μm"
    plt.semilogy(theta_deg, SU, label=f"{label}")

plt.xlim(0, 180)
plt.xticks(np.arange(0, 181, 30))
plt.tick_params(which='both', direction='in')
plt.xlabel("Scattering angle (ϴ)", fontsize=16)
plt.ylabel("Intensity ($\mathregular{|S|^2}$)", fontsize=16, labelpad=10)
plt.legend(loc='upper right')
plt.title(f"Scattering Intensity for Different Radii at λ={w}nm (Unpolarized)", fontsize=18)
plt.tight_layout()
plt.show()