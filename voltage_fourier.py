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

# Calculate the voltage
voltage_Patch1 = elec_Energy1 / elec_Charge1

# Perform FFT analysis
dt = time[1] - time[0]  # Time step
N = len(time)  # Number of data points
freq = np.fft.fftfreq(N, dt)  # Frequency values
fft_values = np.fft.fft(voltage_Patch1)  # FFT of the voltage data

freq = np.fft.fftshift(freq)
fft_values = np.fft.fftshift(fft_values)

# Plot the frequency-domain data
plt.figure(figsize=(10, 6))
plt.plot(freq, np.abs(fft_values), linestyle='-', color='b', linewidth=1.0, label='Patch 1')
plt.xlim(0, 1 / (2 * dt))  # Limit to the Nyquist frequency
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.title('FFT Analysis of Voltage at patch 1')
plt.legend(loc='best')
plt.grid(True)

plt.savefig("voltage_fourier.png")

plt.show()