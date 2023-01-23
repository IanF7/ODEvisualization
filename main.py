# Ian Fletcher
# CST-305
# 1/22/2023
# Visualizing ODEs with SciPy

# Imports NumPy, SciPy odeint package, and matplotlib
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# p is number of packages
# t is time in seconds
# dp_dt is throughput
# Define equation dp_dt used to calculate throughput given p and t
def dp_dt(p, t):
    # k is a constant packet size in kilobyte (kb)
    k = 0.5
    return k * t


# p0 is initial number of packets
p0 = 0
# Uses linspace to generate datapoints
t = np.linspace(0, 300, 1000)
# sets p equal to odeint given the inputs for results
p = odeint(dp_dt, p0, t)

# uses matplotlib to plot datapoints with time on the x-axis and packets on the y-axis
plt.plot(p, t)
plt.xlabel('packets')
plt.ylabel('time')
plt.show()


