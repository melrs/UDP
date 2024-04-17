import socket

HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
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

