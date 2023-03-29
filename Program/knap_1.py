from bateri_niveau import bat_level
from machine import Pin
from time import sleep

# Led objects
red_led = Pin(5, Pin.OUT)
yellow_led = Pin(18, Pin.OUT)
green_led = Pin(19, Pin.OUT)

def pressed_zero():
    red_led.on()
    green_led.on()
    sleep(0.5)
    red_led.off()
    green_led.off()
    
    
def pressed_once():
    # battery leve found in file bateri_niveau.
    # if battery is less than 3.4 red led will turn on.
    if bat_level() <= 3.4:
        red_led.on()
        sleep(2)
        red_led.off()
    # if battery level less than 3.8 both red and yellow led turn on.    
    elif bat_level() <= 3.8:
        red_led.on()
        yellow_led.on()
        sleep(2)
        red_led.off()
        yellow_led.off()
    # if battery lebel is above 3.8 all led will turn on.    
    else:
        red_led.on()
        yellow_led.on()
        green_led.on()
        sleep(2)
        red_led.off()
        yellow_led.off()
        green_led.off()