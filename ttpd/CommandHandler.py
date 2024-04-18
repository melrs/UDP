
from abc import ABC, abstractmethod
import socket

class CommandHandler(ABC):
    
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def handle(self, server_socket: socket.socket, addr):
        pass
