import simple_gps_example as gps
import network
from netværk import mac_adress
#from machine import RTC
import reciever

#rtc = RTC()


def get_locate(gpslot, gpslat):
    global lot
    global lat
    lot=gpslot
    lat=gpslat
    print(gpslot)

def get_time_and_date(gps_date, gps_time):
    global time
    global date
    date=gps_date
    time=gps_time

def pressed_third():
    global lot
    global lat
    global date
    global time
    deviceID = 1
    macAdd = mac_adress()
    #time = rtc.datetime()
    curTime = str(str(date) + ' - ' +
                  str(time[0]) + ':' + str(time[1]) + ':' + str(time[2]))
    
    print(curTime)
    #print(lot)
    reciever.init_data(deviceID, lot, lat, macAdd, curTime)

    

    #simple_gps_example.latitude_string()
    #simple_gps_example.longitude_string()
    #print(simple_gps_example.latitude_string())
    #print(simple_gps_example.longitude_string())
