import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt



def FFT(y,sample_time):

    sample_rate = 1000000/sample_time  # Sample rate in Hz
    T = 1.0 / sample_rate  # Sample spacing
    N = len(y)
     

    yf = np.fft.fft(y)
    xf = np.fft.fftfreq(N, T)
    yf_abs = np.abs(yf)
    xf = xf[:N//2]
    yf_abs = yf_abs[:N//2]


    plt.plot(xf, yf_abs)
    plt.title('Frequency Domain')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid()
    plt.show()
    

# yy = np.array([np.sin(2 * np.pi * 120 * t/1000) + 0.5 *np.sin(2 * np.pi * 80 * t/1000) + 0.2 *np.sin(2 * np.pi * 190 * t/1000) for t in range(1000)])
#FFT(yy,80)

