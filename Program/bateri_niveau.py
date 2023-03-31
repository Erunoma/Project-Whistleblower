from machine import Pin, SoftI2C
from time import sleep

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=1000000)

device_address  = 0x49
#findes ved at tage en måling på sit batteri, kaldet U
#U*1023/adc_val = u_num
u_num = 6.6
#6.5

def bat_level():
   
    adc_bytes = i2c.readfrom(device_address, 2)
    
    #Her printes de enkelte adc bytes
    print("adc_byte 0          ",hex(adc_bytes[0]))
    print("acd byte 0, bit 1-0 ", hex(adc_bytes[0] & 0x03))
    print("acd byte 0, bit 3-2 ", hex((adc_bytes[0] >> 2) & 0x03))
    print("adc_byte 1          ",hex(adc_bytes[1]))      
    print("adc_byte 1, bit 7-2 ",hex(adc_bytes[1]>>2))
    
    #Low_byte består af acd_byte[0] 1-0 og acd_byte[1] 7-2
    lowByte = ((int(adc_bytes[0]) << 6) & 0xC0) + (int(adc_bytes[1]) >> 2)
    print("Low byte:           ", hex(lowByte))
    highByte = (int(adc_bytes[0]) >> 2)
    print("high byte:          ", hex(highByte))      
    adc_val = (highByte << 8) + lowByte
    print("adc value  i hex     ", hex(adc_val))
    print("adc value i int      ", int(adc_val))
    
    #omregning af adc værdi til spænding og print
    voltage = (adc_val * u_num) / 1023.0
    print("spænding             ",voltage)
    
    return voltage

    
