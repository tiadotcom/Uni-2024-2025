import numpy as np
import matplotlib.pyplot as plt

# Signal generation
t = np.linspace(0, 1, 1000)  # Time array
y = np.cos(2 * np.pi * t) + np.cos(2 * np.pi * 12 * t)  # Composite signal

# Compute FFT and frequencies
yFFT = np.fft.fft(y)
freq = np.fft.fftfreq(len(t), t[1] - t[0])

# Plot original signal and its spectrum
fig, A = plt.subplots(2, 1, figsize=(10, 5))
A[0].plot(t, y, label='Original Signal')
A[0].set_xlabel('Time (s)')
A[0].set_ylabel('Amplitude')
A[1].plot(freq, np.abs(yFFT), label='Spectrum')
A[1].set_xlim(-19, 19)
A[1].set_xlabel('Frequency (Hz)')
A[1].set_ylabel('Amplitude')

# Apply frequency filter
Freq_lim = 10  # Frequency limit
for i in range(len(freq)):
    if np.abs(freq[i]) < Freq_lim: # Change ">" to "<" in order to apply the low pass filter
        yFFT[i] = 0

# Compute inverse FFT of the filtered signal
yFilt = np.fft.ifft(yFFT)

# Plot filtered signal
A[0].plot(t, yFilt, label='Filtered Signal')
A[0].legend()
plt.tight_layout()
plt.show()
