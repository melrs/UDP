from abc import ABC, abstractmethod
from UDPSocket import UDPSocket

class CommandHandler(ABC):
    
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def handle(self, server_socket: UDPSocket):
        pass
