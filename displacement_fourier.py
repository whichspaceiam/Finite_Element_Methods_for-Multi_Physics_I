import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

file_path = "job_transient-mechDisplacement-node-604-N_PlateCenter.txt"

# Read data from the file
data = np.loadtxt(file_path, skiprows=3)

# Extract columns
time = data[:, 0]
z_ampl = data[:, 3]

# Displacement along z-axis
displacement = z_ampl

# Perform FFT analysis
dt = time[1] - time[0]  # Time step
N = len(time)  # Number of data points
freq = np.fft.fftfreq(N, dt)  # Frequency values
fft_values = np.fft.fft(displacement)  # FFT of the displacement data

freq = np.fft.fftshift(freq)
fft_values = np.fft.fftshift(fft_values)


# Plot the frequency-domain data
plt.figure(figsize=(10, 6))
plt.plot(freq, np.abs(fft_values), linestyle='-', color='b', linewidth=1.0, label='Displacement along z-axis (3-direction)')
plt.xlim(0, 1 / (2 * dt))  # Limit to the Nyquist frequency
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.title('FFT Analysis of Displacement at the central node')
plt.legend(loc='best')
plt.grid(True)

plt.savefig("displacement_fourier.png")
plt.show()