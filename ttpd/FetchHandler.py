from config import BUFFER_SIZE
from ttpd.CommandHandler import CommandHandler
from ttpd.Package import Package
from utils import build_package
from UDPSocket import UDPSocket

class FetchHandler(CommandHandler):
    
    def handle(self, server_socket: UDPSocket):
        try:
            print(f"Sending file {self.filename}")
            with open(self.filename, 'rb') as file:
                i = 0
                while True:
                    chunk = file.read(BUFFER_SIZE)
                    i += 1
                    if not chunk:
                        server_socket.send_sucess_message(i, "File sent")
                        break
                    server_socket.sendto(i, chunk)
        except FileNotFoundError:
            server_socket.send_error_message("ERROR - File not found")
    

