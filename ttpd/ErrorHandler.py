
import socket
from ttpd.CommandHandler import CommandHandler


class ErrorHandler(CommandHandler):
    
    def handle(self, server_socket: socket.socket, buffer_size: int):
        try:
            with open(self.filename, 'rb'):
                yield "File exists".encode()
        except FileNotFoundError:
            yield "ERROR - File not found".encode()
