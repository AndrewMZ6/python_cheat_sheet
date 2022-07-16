import socket

HOST = 'localhost'
PORT = 5001

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((HOST, PORT))

sc.send("HELLO!".encode('utf-8'))
print(sc.recv(1024).decode('utf-8'))

### output
#>>> I received your message. TY!