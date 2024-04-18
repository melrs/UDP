import socket
from config import HOST, PORT, BUFFER_SIZE
from ttpd_protocol import handle_request

def setup_server_socket(host, port, buffer_size):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, BUFFER_SIZE)
    return server_socket

server_socket = setup_server_socket(HOST, PORT, BUFFER_SIZE)
print('Servidor UDP pronto para receber conexões...')

while True:
    data, addr = server_socket.recvfrom(BUFFER_SIZE)
    request = data.decode()
    
    if ' ' not in request:
        raise ValueError('Required format: COMMAND filename')
    
    print('Mensagem recebida:', request)
    
    for response in handle_request(data):
        server_socket.sendto(response, addr)
        print('Resposta enviada:', response.decode())



