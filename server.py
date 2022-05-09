import socket

HOST = '192.168.0.13'
PORT = 12311

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    comm, addr = server.accept()
    print(f'created socket {comm}')
    print(f'connected to client {addr}')
    message = comm.recv(1024).decode('utf-8')
    print(f'got message {message}')
    comm.send('I received your message. TY!'.encode('utf-8'))
    comm.close()
    print(f'connection with client {addr} closed')