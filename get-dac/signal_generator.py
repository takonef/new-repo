import numpy as np
import time
import math

def get_sin_wave_amplitude(freq, time):
    y = math.sin(2*math.pi*freq*time)
    amplitude = 