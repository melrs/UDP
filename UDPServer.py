import socket
from config import HOST, PORT, BUFFER_SIZE
from ttpd_protocol import TTPDProtocol
from utils import calculate_checksum

class UDPServer:
    def __init__(self, host, port, buffer_size):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.server_socket = None
        self.ttpd_protocol = TTPDProtocol()

    def setup_server_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, self.buffer_size)

    def start(self):
        self.setup_server_socket()
        print('Servidor UDP pronto para receber conexões...')

        while True:
            data, addr = self.server_socket.recvfrom(self.buffer_size)
            request = data.decode()

            if ' ' not in request:
                raise ValueError('Required format: COMMAND filename')

            print('Mensagem recebida:', request)

            for response in self.ttpd_protocol.handle_request(data).handle():
                self.server_socket.sendto(response, addr)
                print('Resposta enviada:', response.decode())

server = UDPServer(HOST, PORT, BUFFER_SIZE)
server.start()


