import socket
import serial
import time
HOST = '84.237.53.150' # мой IP 84.237.53.150
PORT = 27016 # мой порт 27016

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
ser = serial.Serial('COM6', 9600) # Вместо COM4 укажи свой порт
while True:
    time.sleep(0.01)
    data = s.recv(100)
    string = data.strip().decode('utf-8')
    print('Boyko is calling')
    ser.write(string.encode())
    arduinoData = ser.readline().strip().decode('utf-8')
    # arduinoData = ser.readline()
    print(arduinoData)


    s.send(bytes(arduinoData, 'utf-8'))
    # s.send(bytes(arduinoData))














#
#
# from serial.tools import list_ports
#

# # while(1):
# #     # print(ser.readline().strip().decode('utf-8'))
# #     string = str.encode('SHEFER IS HERE')
# #     print(ser.write(format(('{}\n').format(string)).encode()))
# #     # my_decoded_str = string.decode('utf-8')
# #     # print(my_decoded_str)
# #     # print(ser.write(my_decoded_str))
# #     last_msg = ""
# ser = serial.Serial('COM6', 9600, timeout=1)
# while 1:
#     #value = 5
#     string = 'SHEFER IS HERE'
#     ser.write(string.encode())
#     arduinoData = ser.readline().strip().decode('utf-8')
#     print(arduinoData)
#     time.sleep(1)
