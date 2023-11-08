import PyMieScatt as ps
import numpy as np
import matplotlib.pyplot as plt

m = 1.33257 + 1.67E-08j    # Refractive index
w = 532                    # Wavelength in nanometers
r = 1000                   # Radius in nanometers
d = 2*r  

theta, SL, SR, SU = ps.ScatteringFunction(m, w, d)
theta_deg = theta*(180/np.pi)
plt.figure(figsize=(10, 6))

plt.semilogy(theta_deg, SR, 'g--', lw=1, label="Parallel Polarization")
plt.semilogy(theta_deg, SL, 'g', lw=1, label="Perpendicular Polarization")
# Create a table to display parameter values
columnLabels = ['Input Parameters','Values']
tableValues = [['Wavelength λ', f' {w} nm'], ['Radius of particle(r)', f'{r/1000} µm'],['Ref. Index(m)',m],]
my_table = plt.table(cellText=tableValues,
                    colWidths=[0.16,0.16],
                    colLabels=columnLabels,
                    loc='lower left')
plt.xlim(0, 180)
plt.xticks(np.arange(0, 181, 30))
plt.tick_params(which='both', direction='in')
plt.xlabel("Scattering angle(ϴ)", fontsize=16)
plt.ylabel("Intensity ($\mathregular{|S|^2}$)", fontsize=16, labelpad=10)
plt.legend()
plt.title("Scattering Intensity Functions", fontsize=18)
plt.tight_layout()
plt.show()