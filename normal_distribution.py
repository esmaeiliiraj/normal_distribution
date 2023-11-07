import numpy as np
import scipy
import matplotlib.pyplot as plt

# Gaussian/Normal Distribution

# Standard Gaussian has a mean of zero and variance of 1. Try different values!
# Gaussian parameters
mu = 2
var = 5

# x values. About 95% of the area of a Gaussian falls between 2*sigma around the mean. So, 3.5*sigma will be good!
x = np.linspace(mu-(3.5*np.sqrt(max(var,1))), mu+(3.5*np.sqrt(max(var,1))), 1000)

# Gaussian PDF
f = (1/np.sqrt(2*np.pi*var)) * np.e**(np.square(x-mu)/(-2*var))

# Standard Gaussian
f_stand = (1/np.sqrt(2*np.pi*1)) * np.e**(np.square(x-0)/(-2*1))

# Plotting values
plt.plot(x, f, color="red", label=f"Normal (mu={mu}, var={var})")
plt.plot(x, f_stand, color="grey", linestyle="--", label="Standard Normal")
plt.xlim(left=min(x), right=max(x))
plt.ylim(bottom=min(f.min(),f_stand.min())-0.02, top=max(f.max(),f_stand.max())+0.05)
plt.xlabel("X")
plt.ylabel("PDF")
plt.legend();
