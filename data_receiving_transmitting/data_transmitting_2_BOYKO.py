import serial
import time
import struct

ser = serial.Serial('COM5') # Вместо COM5 укажи свой порт
coi = 0
while True:
    data = ser.readline()
    time.sleep(0.01)
    datum1 = '10'
    #ser.write(datum1.encode())
    ser.write(struct.pack('>BBBB',45,90,180, 255))
    print(data.strip().decode('utf-8'))
'''
    if coi < 10:
        coi += 1
    else:
        print(data.strip().decode('utf-8'))
    '''



    #ser.write(datum1.encode())
    #print(data.strip().decode('utf-8'))
