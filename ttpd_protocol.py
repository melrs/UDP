from ttpd.CheckHandler import CheckHandler
from ttpd.CommandHandler import CommandHandler
from ttpd.ErrorHandler import ErrorHandler
from ttpd.FetchHandler import FetchHandler

class TTPDProtocol:
    
    def __init__(self):
        pass

    def resolve(self, data) -> CommandHandler:
        request = data.decode()
        command, filename = request.split(maxsplit=1)

        match command:
            case 'FETCH':
                return FetchHandler(filename)
            case 'CHECK':
                return CheckHandler(filename)
            case _:
                return ErrorHandler(filename)
