import time
from TTPD.CommandHandler import CommandHandler
from UDP.UDPSocket import UDPSocket
from commons.config import BUFFER_SIZE
from commons.utils import get_package_minimun_size

class FetchHandler(CommandHandler):
    
    def handle(self, server_socket: UDPSocket):
        try:
            print(f"Fetching file {self.filename}")
            print(self.packages_to_send)
            is_recovery_fetch = bool(self.packages_to_send)
            with open(self.filename, 'rb') as file:
                i = 0
                while True:
                    chunk = file.read(BUFFER_SIZE - get_package_minimun_size(i))
                    i += 1
                    if not chunk:
                        server_socket.send_sucess_message(i, "File sent")
                        break
                    if is_recovery_fetch:
                        print(f"Sending package {i}")
                        if str(i) not in self.packages_to_send:
                            print(f"Skipping package {i}")
                            continue
                    server_socket.sendto(i, chunk)
        except FileNotFoundError:
            server_socket.send_error_message("ERROR - File not found")
    

