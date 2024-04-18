from UDPSocket import UDPSocket
from ttpd.CommandHandler import CommandHandler

class ErrorHandler(CommandHandler):
    
    def handle(self, server_socket: UDPSocket):
        server_socket.send_error_message("ERROR - Command not found")
