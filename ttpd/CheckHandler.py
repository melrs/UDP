
import socket
from ttpd.CommandHandler import CommandHandler

class CheckHandler(CommandHandler):
    
    def handle(self, server_socket: socket.socket, addr):
        try:
            print(f"Sending error message for {self.filename}")
            with open(self.filename, 'rb'):
                server_socket.sendto("File exists".encode(), addr)
        except FileNotFoundError:
            error = "ERROR - File not found".encode()
            server_socket.sendto(error, addr)
