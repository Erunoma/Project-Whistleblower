from bateri_niveau import bat_level
from machine import Pin
from time import sleep

# Led objekter
red_led = Pin(19, Pin.OUT)
yellow_led = Pin(17, Pin.OUT)
green_led = Pin(5, Pin.OUT)


def pressed_once():
    # er batteri niveau bliver hentet fra fil bateri_niveau.
    # er niveauet under 3.4 , vil rød led lyse.
    if bat_level() <= 3.4:
        red_led.on()
        sleep(2)
        red_led.off()
    # er bateri niveau under 3.8 vil både rød og gul led lyse.    
    elif bat_level() <= 3.8:
        red_led.on()
        yellow_led.on()
        sleep(2)
        red_led.off()
        yellow_led.off()
    # er bateri niveauet over 3.8 vil alle 3 leder lyse    
    else:
        red_led.on()
        yellow_led.on()
        green_led.on()
        sleep(2)
        red_led.off()
        yellow_led.off()
        green_led.off()