import socket

HOST = '84.237.53.150' # мой IP 84.237.53.150
PORT = 27016 # мой порт 27016

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

while True:
    data = s.recv(100)
    print(data)
