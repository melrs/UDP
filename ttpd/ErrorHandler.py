
import socket
from ttpd.CommandHandler import CommandHandler

class ErrorHandler(CommandHandler):
    
    def handle(self, server_socket: socket.socket, buffer_size: int):
        try:
            print(f"Sending error message for {self.filename}")
            with open(self.filename, 'rb'):
                yield "File exists".encode()
        except FileNotFoundError:
            yield "ERROR - File not found".encode()
