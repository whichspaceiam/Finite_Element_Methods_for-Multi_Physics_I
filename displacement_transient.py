import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

file_path = "job_transient-mechDisplacement-node-604-N_PlateCenter.txt"

# Read data from the file
data = np.loadtxt(file_path, skiprows=3)

# Extract columns
time = data[:, 0]
x_ampl = data[:, 1]
y_ampl = data[:, 2]
z_ampl = data[:, 3]

#displacement = np.sqrt(x_ampl**2 + y_ampl**2 + z_ampl**2)
displacement = z_ampl
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time, displacement, linestyle='-', color='b', linewidth=1.0, label='Displacement along z-axis (3-direction)')
#plt.ylim(0, 2.7e-5)
plt.xlim(0,0.5)
#plt.xticks(np.arange(0, 501, 50))
plt.xlabel('time [s]')
plt.ylabel('Displacement [m]')
plt.title('Displacement at the central node of the PMMA-Plate')
plt.legend(loc='best')
plt.grid(True)

plt.savefig("displacement_transient.png")
plt.show()