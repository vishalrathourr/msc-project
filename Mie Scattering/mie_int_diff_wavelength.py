import PyMieScatt as ps
import numpy as np
import matplotlib.pyplot as plt

# Input parameters
refractive_index = 1.33257 + 1.67E-08j
radius = 1000  # Radius in nanometers
wavelengths = [532, 650, 800]  # Wavelengths in nanometers

# Create a figure
fig, ax = plt.subplots(figsize=(12, 8))

# Loop over wavelengths
for w in wavelengths:
    d = 2 * radius  # Diameter

    # Calculate scattering intensity
    theta, SL, SR, SU = ps.ScatteringFunction(refractive_index, w, d)
    theta_deg = theta * (180 / np.pi)

    # Plot the scattering intensity
    ax.semilogy(theta_deg, SU, label=f'λ = {w} nm')

# Create a table inside the graph to display parameter values
column_labels = ['Input Parameters', 'Values']
table_values = [['Ref. Index (m)', refractive_index], ['Radius (r)', f'{radius/1000} µm']]
table = ax.table(cellText=table_values,
                 colWidths=[0.16, 0.16],
                 colLabels=column_labels,
                 loc='lower left', bbox=[0.015, 0.015, 0.24, 0.2])

# Customize the plot
ax.set_xlim(0, 180)
ax.set_xticks(np.arange(0, 181, 30))
ax.tick_params(which='both', direction='in')
ax.set_xlabel("Scattering angle (ϴ)", fontsize=16)
ax.set_ylabel("Intensity ($|S|^2$)", fontsize=16, labelpad=10)
ax.legend()
ax.set_title("Scattering Intensity Functions for Multiple Wavelengths(Unpolarized)", fontsize=18)

plt.tight_layout()
plt.show()
