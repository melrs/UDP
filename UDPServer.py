import socket
from UDPSocket import UDPSocket
from config import HOST, PORT, BUFFER_SIZE
from ttpd_protocol import TTPDProtocol
from utils import calculate_checksum

class UDPServer:
    def __init__(self, host, port, buffer_size):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.server_socket = UDPSocket()
        self.ttpd_protocol = TTPDProtocol()

    def start(self):
        print('Servidor UDP pronto para receber conexões...')

        while True:
            package = self.server_socket.recvfrom()
            data = package.data
            request = data.decode()

            print('Mensagem recebida:', request)

            self.ttpd_protocol.resolve(package).handle(self.server_socket)
            
            data = self.server_socket.recvfrom().data
            print('Resposta do cliente:', data.decode())
            self.ttpd_protocol.resolve(package).handle(self.server_socket)

server = UDPServer(HOST, PORT, BUFFER_SIZE)
server.start()

