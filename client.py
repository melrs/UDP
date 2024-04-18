import socket
from config import HOST, PORT, BUFFER_SIZE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (HOST, PORT)

message = input("Mensagem: ").encode()
sock.sendto(message, server_address)

data, addr = sock.recvfrom(BUFFER_SIZE)
print('Received:', data.decode())

sock.close()
