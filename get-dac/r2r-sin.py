import r2r_dac as r2r
import signal_generator as sg
import time

leds = [16, 20, 21, 25, 26, 17, 27, 22]
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    dac = r2r.R2R_DAC(leds, dynamic_range, True)
    try:

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах:"))
                dac.set_voltage(amplitude*sg.get_sin_wave_amplitude(time.time))
                sg.wait_for_sampling_period(sampling_frequency)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз:")
    finally:
        dac.deinit()
    