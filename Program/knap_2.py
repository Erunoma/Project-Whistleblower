from machine import Pin
from machine import PWM
from time import sleep

# buzzer objekt 
buzzer_pin = Pin(25, Pin.OUT)
pwm_buzz = PWM(buzzer_pin)

# funktionen der fastsætter de forskellige parametre
# som buzzeren skal bruge. så man kan senere kan
# nøjes med at give argumenterne til funktionen 
def buzzer(buzzerPinObject, frequency, sound_duration, silence_duration):
    buzzerPinObject.duty(512)
    buzzerPinObject.freq(frequency)
    sleep(sound_duration)
    buzzerPinObject.duty(0)
    sleep(silence_duration)

# Funktionen der kalder de forskellige toner.
# det er denne funktion der bliver kaldt i main filen. 
def pressed_twice():
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)
    buzzer(pwm_buzz, 440, 0.2, 0.2)

