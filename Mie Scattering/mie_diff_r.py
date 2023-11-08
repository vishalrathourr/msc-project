import PyMieScatt as ps
import numpy as np
import matplotlib.pyplot as plt

m = 1.33257 + 1.67E-08j    # Refractive index
w = 650                    # Wavelength in nanometers
radii = [500, 5000, 50000]  # List of radii in nanometers
theta_deg = np.linspace(0, 180, 100)

plt.figure(figsize=(10, 6))

# Iterate over different radii and plot their scattering intensity functions for both polarizations
for r in radii:
    d = 2 * r
    theta, SL, SR, SU = ps.ScatteringFunction(m, w, d)
    theta_deg = theta * (180 / np.pi)
    label = f"Radius {r/1000} µm"
    plt.semilogy(theta_deg, SU, label=f"{label} (Unpolarized)")
tableValues = [['Wavelength λ', f' {w} nm'],
               ['Refractive Index (m)', f'{m.real:.5f} + {m.imag:.2E}j'],
              ]
my_table = plt.table(cellText=tableValues,
                    colWidths=[0.16,0.17],
                    loc='lower left')
plt.xlim(0, 180)
plt.xticks(np.arange(0, 181, 30))
plt.tick_params(which='both', direction='in')
plt.xlabel("Scattering angle (ϴ)", fontsize=16)
plt.ylabel("Intensity ($\mathregular{|S|^2}$)", fontsize=16, labelpad=10)
plt.legend()
plt.title("Scattering Intensity Functions for Different Radii", fontsize=18)
plt.tight_layout()
plt.show()
