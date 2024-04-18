
import socket
from config import BUFFER_SIZE
from ttpd.CommandHandler import CommandHandler

class FetchHandler(CommandHandler):
    
    def handle(self, server_socket: socket.socket, addr):
        try:
            print(f"Sending file {self.filename} to {addr}")
            with open(self.filename, 'rb') as file:
                while True:
                    chunk = file.read(BUFFER_SIZE)
                    if not chunk:
                        break
                    server_socket.sendto(chunk, addr)
        except FileNotFoundError:
            error = "ERROR - File not found".encode()
            server_socket.sendto(error, addr)
