import socket
import serial
import time

HOST = ''
PORT = 27016

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

clientsocket, address = s.accept()
print(f"Client: {clientsocket},  with address {address}  joined the server!")

ser = serial.Serial('COM5') # Вместо COM5 укажи свой порт

while True:
    data = ser.readline()
    print(data.strip().decode('utf-8'))
    time.sleep(0.01)
    clientsocket.send(data)
