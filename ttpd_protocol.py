from ttpd.CheckHandler import CheckHandler
from ttpd.CommandHandler import CommandHandler
from ttpd.ErrorHandler import ErrorHandler
from ttpd.FetchHandler import FetchHandler
from ttpd.Package import Package

class TTPDProtocol:
    
    def __init__(self):
        pass

    def resolve(self, package: Package) -> CommandHandler:
        match package.method:
            case 'FETCH':
                return FetchHandler(package.data.decode())
            case 'CHECK':
                return CheckHandler(package.data.decode())
            case _:
                return ErrorHandler(package.data.decode())
