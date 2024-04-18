import socket
from config import HOST, PORT, BUFFER_SIZE

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
    print('Mensagem recebida:', request)

    if request.startswith('GET'):
        filename = request.split()[1][1:]
        try:
            with open(filename, 'rb') as file:
                while True:
                    chunk = file.read(BUFFER_SIZE)
                    if not chunk:
                        break
                    server_socket.sendto(chunk, addr)
        except FileNotFoundError:
            error_msg = "Arquivo não encontrado"
            server_socket.sendto(error_msg.encode(), addr)

