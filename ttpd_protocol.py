from ttpd.CheckHandler import CheckHandler
from ttpd.ErrorHandler import ErrorHandler
from ttpd.FetchHandler import FetchHandler

class TTPDProtocol:
    
    def __init__(self):
        pass

    def handle_request(self, data):
        request = data.decode()
        command, filename = request.split(maxsplit=1)

        match command:
            case 'FETCH':
                return FetchHandler(filename)
            case 'CHECK':
                return CheckHandler(filename)
            case _:
                return ErrorHandler(filename)
