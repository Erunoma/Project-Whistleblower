import time
from netværk import net_connect
from knap_1 import pressed_once
#from knap_2 import pressed_twice
#cfrom knap_3 import pressed_third
#from reciver import init_data, send_data
from machine import Pin


# connecting to network
net_connect()


# knap object
button = Pin(12, Pin.IN)
#ventetid inden reset i sekunder
timeout = 5
#antal knaptryk
press_count = 0

# første tidsstempel
start_time = time.time()    

  
# funktionen for styring af tid og tælling af antal tryk.
def script_switch():
    
    global press_count
    global start_time
    
    while True:    
        #forsøg på at begrænse hvor mange tange den kører funktioner
        kør_en_gang = True
        # kode der køre inden for tidsperioden.     
        while (time.time()-start_time) < timeout:
            # debounce fix
            first = button.value()
            time.sleep(0.01)
            second = button.value()
            # tæller, til antal klik    
            if first and not second:
                press_count +=1
                second_time = time.time()
            # hvis der ikke er klikket, sker ingenting
            if press_count == 0:
                pass
            # er der i perioden talt 1 klik, køres funktionen
            # fra knap_1 fil.
            if press_count == 1 and (time.time()-second_time)>1.5:   #her forsøger jeg at få den til at vente 1,5 sek med at se hva count er, så man undgår den kører funktion 1 på vej til funktion to
                if kør_en_gang:
                    pressed_once()
                    kør_en_gang = False
            # er der i perioden talt 2 klik, køres funktionen
            # fra knap_2 fil.        
            if  press_count == 2  and (time.time()-second_time)>1.5:
                if kør_en_gang:
                    #pressed_twice()
                    print('2')
                    kør_en_gang = False
            # er der i perioden talt 3 klik, køres funktionen
            # fra knap_2 fil samt fra knap_3.
            if press_count == 3 and (time.time()-second_time)>1.5:
                if kør_en_gang:
                    #pressed_twice()
                    #pressed_third()
                    #init_data()
                    #send_data()
                    print('3')
                    kør_en_gang = False
        # tæller og timer nulstilles        
        print("nået til slut")
        press_count = 0
        start_time = time.time()  
            
# funktionen bliver kaldt, så koden kan køre.            
script_switch()