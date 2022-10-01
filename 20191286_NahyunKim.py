# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:23:45 2021

@author: kimna
"""

import numpy as np
from matplotlib import pyplot as plt

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds

_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.5

mixed_tone = nice_tone + noise_tone

normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

plt.plot(normalized_tone[:1000], color='blue')
plt.xlabel('Time (s)', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.title("400 Hz distorted sine wave signal with 4000 Hz tone of distortion", fontsize=12)
plt.show()

from scipy.fft import fft, fftfreq

# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION

yf = fft(normalized_tone)
xf = fftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf), color='blue')
plt.xlabel('Frequency [Hz]', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.title("Frequency domain of the signal using fft", fontsize=12)
plt.show()
# The negative-positive symmetry will be caused by inputting real numbers (not complex numbers) to the transform. 
# We can use this symmetry to make your Fourier transform faster by computing only half of it. scipy.fft implements this speed hack in the form of rfft().

from scipy.fft import rfft, rfftfreq

yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf), color='blue')
plt.xlabel('Frequency [Hz]', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.title("Frequency domain of the signal using rfft", fontsize=12)
plt.show()
#rfft() never calculates the negative half of the frequency spectrum, which makes it faster than using fft().

# The maximum frequency is half the sample rate
points_per_freq = len(xf) / (SAMPLE_RATE / 2)
# Our target frequency is 4000 Hz
target_idx = int(points_per_freq * 4000)

yf[target_idx - 1 : target_idx + 2] = 0

plt.plot(xf, np.abs(yf), color='blue')
plt.xlabel('Frequency [Hz]', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.title("Frequency domain of the signal filtering the high-pitched frequency", fontsize=8.5)
plt.show()