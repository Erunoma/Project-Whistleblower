# prevent unwanted buzzing
from machine import Pin, PWM
from knap_2 import buzzer, pressed_twice
# buzzer object 
buzzer_pin = Pin(26, Pin.OUT)
pwm_buzz = PWM(buzzer_pin)
buzzer(pwm_buzz, 440, 0, 0)

import time
import _thread
from simple_gps_example import gps_main
from netværk import net_connect, mac_adress
from knap_1 import pressed_zero, pressed_once
from knap_3 import pressed_third



# connecting to network
net_connect()


# GPS start
_thread.start_new_thread(gps_main, ())

print('hello')
# button object
button = Pin(26, Pin.IN)
# wait time in sekunder
timeout = 5
# number of button presses
press_count = 0

# first timestamp
#start_time = time.time()    


# function for time and button count.
def script_switch():
    global press_count
    #global start_time
    start_time = time.time() 
                    
    while True:
        print('hello1')
        # variable to stop loop
        kør_en_gang = True
        # time loop for button count and running scripts,
        # depending on number of button presses. 
        while (time.time()-start_time) < timeout:
            #print('hello2')
            # debounce fix
            first = button.value()
            time.sleep(0.01)
            second = button.value()
            # counter, for number of button presses.    
            if first and not second:
                press_count +=1
                second_time = time.time()
            # if button press is 0, nothing happens
            if press_count == 0 and (time.time()-start_time)>3:
                pressed_zero()
                kør_en_gang = False
            # if button press is 1 the function runs knap_1 file.
            if press_count == 1 and (time.time()-second_time)>1.5:   #her forsøger jeg at få den til at vente 1,5 sek med at se hva count er, så man undgår den kører funktion 1 på vej til funktion to
                if kør_en_gang:
                    pressed_once()
                    kør_en_gang = False
            # if button press is 2 the function runs knap_2 file.
            if  press_count == 2  and (time.time()-second_time)>1.5:
                if kør_en_gang:
                    pressed_twice(pwm_buzz)
                    print('2')
                    kør_en_gang = False
            # if button press is 3 the function runs knap_2
            # and knap_3 file, and sends the data.
            if press_count == 3 and (time.time()-second_time)>1.5:
                if kør_en_gang:
                    pressed_twice(pwm_buzz)
                    pressed_third()
                    #print(mac_adress())
                    print('3')
                    kør_en_gang = False
        # counter and timer is reset.         
        print("nået til slut")
        press_count = 0
        start_time = time.time()  
                    
script_switch()
# starting gps connection and main script
#_thread.start_new_thread(script_switch, ())