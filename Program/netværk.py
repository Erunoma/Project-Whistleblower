import ubinascii
import network
import urequests
from time import sleep

import esp
esp.osdebug(None)
import gc
gc.collect()


# Network credentials
ssid = 'Watson'
password = 'Knufk8h#'


# function is called in main file.
def net_connect():
    try:
        
        # For ESP to connect
        station = network.WLAN(network.STA_IF)
        station.active(True)
        station.connect(ssid, password)
    except:
        while station.isconnected() == False:
            print('.', end='')
            sleep(0.2)
    
    # printing feedback, ip and mac
    print('Connection successful')
    #print(station.ifconfig())

def mac_adress():
    wlan_sta = network.WLAN(network.STA_IF)
    wlan_sta.active(True)
    wlan_mac = wlan_sta.config('mac')
    return ubinascii.hexlify(wlan_mac, ':').decode().upper()
 
# Code is from "Micropython EPS32 and ESP8266"
# by Rui Santos and Sara Santos, modul 4 page 254