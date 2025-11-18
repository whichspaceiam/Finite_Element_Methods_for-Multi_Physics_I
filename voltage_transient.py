import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

# Patch 1
patch1_1 = "job_transient-elecEnergy-region-V_Patch1.txt"
data1_1 = np.loadtxt(patch1_1, skiprows=3)

# Extract columns
time = data1_1[:, 0]
elec_Energy1 = data1_1[:, 1]

patch1_2 = "job_transient-elecCharge-surfRegion-S_top_Patch1.txt"
data1_2 = np.loadtxt(patch1_2, skiprows=3)

# Extract columns
elec_Charge1 = data1_2[:, 1]

#Calculate the voltage
voltage_Patch1 = elec_Energy1/elec_Charge1

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time, voltage_Patch1, linestyle='-', color='b', linewidth=1.0, label='Patch 1')
#plt.ylim(0, 2.7e-5)
plt.xlim(0,0.5)
#plt.xticks(np.arange(0, 501, 50))
plt.xlabel('time [s]')
plt.ylabel('Voltage [V]')
plt.title('Voltage vs. time at patch 1')
plt.legend(loc='best')
plt.grid(True)

plt.savefig("voltage_transient.png")
plt.show()