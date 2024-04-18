
from ttpd.CommandHandler import CommandHandler


class CheckHandler(CommandHandler):
    
    def handle(self):
        try:
            with open(self.filename, 'rb'):
                yield "File exists".encode()
        except FileNotFoundError:
            yield "ERROR - File not found".encode()
