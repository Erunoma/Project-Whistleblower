from machine import Pin
from machine import PWM
from time import sleep

# buzzer object 
#buzzer_pin = Pin(27, Pin.OUT, value=0)
#pwm_buzz = PWM(buzzer_pin)

# function that contain the arguments the buzzer needs. 
# later it's just a questino to give the arguments to the function.
def buzzer(buzzerPinObject, frequency, sound_duration, silence_duration):
    buzzerPinObject.duty(512)
    buzzerPinObject.freq(frequency)
    sleep(sound_duration)
    buzzerPinObject.duty(0)
    sleep(silence_duration)

# Buzzer function calling the different notes.
# it is the pressed_twice() function that is called in
# the main file. 
def pressed_twice(pwm_buzz):
    """takes a pwm_buzz object"""
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)


