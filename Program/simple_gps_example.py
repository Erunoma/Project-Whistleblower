from machine import UART
from micropyGPS import MicropyGPS
import time
import knap_3

def gps_main():
    uart = UART(2, baudrate=9600, bits=8, parity=None,
                stop=1, timeout=5000, rxbuf=1024)
    gps = MicropyGPS()
    while True:
        buf = uart.readline()
        #print(buf)
        if buf:
            for char in buf:
    # Note the conversion to to chr, UART outputs ints normally
                gps.update(chr(char))
            #print('UTC Timestamp:', gps.timestamp)
            #print('Date:', gps.date_string('long'))
            #print('Satellites:', gps.satellites_in_use)
            #print('Altitude:', gps.altitude)
            #print('Latitude:', gps.latitude_string())
            #print('Longitude:', gps.longitude_string())
            #print('Horizontal Dilution of Precision:', gps.hdop)
            
            formattedlat = gps.latitude_string()
#             print(formattedlat + "tests")
            formattedlat = formattedlat[:-3]
            formattedlon = gps.longitude_string()
            formattedlon = formattedlon[:-3]
            #print(formattedlon)
            formattedtime = gps.timestamp
            formatteddate = gps.date_string('long')
            knap_3.get_locate(formattedlon, formattedlat)
            knap_3.get_time_and_date(formatteddate, formattedtime)
            #print(formatteddate)
            #print(formattedtime)
            
            #print('lat:', formattedlat)s
            #print('lon:', formattedlon)
            
            time.sleep(2)

#gps_main()



