import socket
from time import sleep

HOST = 'localhost'
PORT = 5001

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((HOST, PORT))

print(f"connection is ready!:\n\n{sc}")


sleep(1)
sc.send("HELLO!".encode('utf-8'))
print(f"got response from server socket!\n\n{sc.recv(1024).decode('utf-8')}")

sc.send("\n".encode('utf-8'))

### output
#>>> I received your message. TY!