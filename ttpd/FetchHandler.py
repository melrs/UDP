
import socket
from config import BUFFER_SIZE
from ttpd.CommandHandler import CommandHandler

class FetchHandler(CommandHandler):
    
    def handle(self, server_socket: socket.socket, buffer_size: int):
        try:
            with open(self.filename, 'rb') as file:
                while True:
                    chunk = file.read(BUFFER_SIZE)
                    if not chunk:
                        break
                    yield chunk
        except FileNotFoundError:
            yield "ERROR - File not found".encode()
