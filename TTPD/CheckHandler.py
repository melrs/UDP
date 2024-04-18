from TTPD.CommandHandler import CommandHandler
from UDP.UDPSocket import UDPSocket

class CheckHandler(CommandHandler):
    
    def handle(self, server_socket: UDPSocket):
        try:
            print(f"Sending error message for {self.filename}")
            with open(self.filename, 'rb'):
                server_socket.send_sucess_message("File exists")
        except FileNotFoundError:
            server_socket.send_error_message("ERROR - File not found")
