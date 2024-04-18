import socket
from config import COUNTINUE_CODE, ERROR_CODE, HOST, PORT, BUFFER_SIZE, SUCCESS_CODE
from ttpd.Package import Package
from utils import build_package

class UDPSocket:
    _instance = None
    
    def __init__(self):
        self.socket = self._setup_socket()

    def _setup_socket(self, buffer_size: int = BUFFER_SIZE):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((HOST, PORT))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, buffer_size)
        return sock
    
    def recvfrom(self, buffer_size: int = BUFFER_SIZE) -> Package:
        self.data, self.addr = self.socket.recvfrom(buffer_size)
        return Package.decode(self.data)
    
    def send_error_message(self, message):
        self.socket.sendto(build_package(-1, message.encode(), ERROR_CODE), self.addr)

    def send_sucess_message(self, id: int, message):
        self.socket.sendto(build_package(id, message.encode(), SUCCESS_CODE), self.addr)
    
    def sendto(self, id: int, data):
        self.socket.sendto(build_package(id, data, COUNTINUE_CODE), self.addr)