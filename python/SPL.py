import numpy as np

def calculate_rms(sound_wave):
    """Calculate the RMS value of a sound wave."""
    sound_wave = [int(i/10.23) for i in sound_wave]
    sensivity = 0.01

    return np.sqrt(np.mean(np.square(sound_wave)))

def calculate_spl(sound_wave, p0=20e-6):
    """Calculate the Sound Pressure Level (SPL) in dB."""
    rms_pressure = calculate_rms(sound_wave)
    spl = 20 * np.log10(rms_pressure / p0)
    return spl
    # return f"Sound Pressure Level (SPL): {spl:.2f} dB"
