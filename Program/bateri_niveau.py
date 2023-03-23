from machine import Pin, ADC
from time import sleep

# pin objekt
analog_pin = ADC(Pin(34))
# ADC range
analog_pin.atten(ADC.ATTN_11DB)
# number of bits.
analog_pin.width(ADC.WIDTH_12BIT)


# reading feed pin, converting to Volt, and print
# in shell.
def bat_level():
    analog_val = analog_pin.read()
    print('Raw analog value: ', analog_val)
    volts = (analog_val * 0.00095078)*5
    print ('The voltage is: ', volts, 'v') 
    return volts
    
    