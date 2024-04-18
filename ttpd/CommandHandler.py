from abc import ABC, abstractmethod
from UDPSocket import UDPSocket
from ttpd.Package import Package

class CommandHandler(ABC):
    
    def __init__(self, package: Package):
        self.package = package
        message = package.data.decode().split(" ")
        print(message)
        self.filename = message[0]
        self.packages_to_send = self.package.data.decode().split(" ")[1:]

    @abstractmethod
    def handle(self, server_socket: UDPSocket):
        pass
