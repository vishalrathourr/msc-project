import PyMieScatt as ps
import numpy as np
import pandas as pd

m = 1.33257 + 1.67E-08j    # Refractive index
w = 630                   # Wavelength in nanometers
r = 1000                   # Radius in nanometers
d = 2*r  

theta, SL, SR, SU = ps.ScatteringFunction(m, w, d, angularResolution=0.1)
theta_deg = theta*(180/np.pi)
data = {
    "Angle(degree)":theta_deg,
    "Perpendicular":SL,
    "Parallel":SR,
    "Unpolarized":SU
}
#Create a dataframe 
df = pd.DataFrame(data)

#Save the data in CSV format in current directory
df.to_csv("Mie Scattering Data")