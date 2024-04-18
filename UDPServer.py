import socket
from UDPSocket import UDPSocket
from config import HOST, PORT, BUFFER_SIZE
from ttpd_protocol import TTPDProtocol

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
            print('Mensagem recebida:', package.data.decode())
            self.ttpd_protocol.resolve(package).handle(self.server_socket)

server = UDPServer(HOST, PORT, BUFFER_SIZE)
server.start()

