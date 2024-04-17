import socket

SERVER_PORT = 12345
BUFFER_SIZE = 1024
HOST = 'localhost'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (HOST, SERVER_PORT)

message = input("Mensagem: ").encode()
sock.sendto(message, server_address)

data, addr = sock.recvfrom(BUFFER_SIZE)
print('Received:', data.decode())

sock.close()
