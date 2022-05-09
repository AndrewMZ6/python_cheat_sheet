import socket

HOST = '192.168.0.13'
PORT = 12311

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((HOST, PORT))

sc.send("HELLO!".encode('utf-8'))
print(sc.recv(1024).decode('utf-8'))