from ttpd.CheckHandler import CheckHandler
from ttpd.CommandHandler import CommandHandler
from ttpd.ErrorHandler import ErrorHandler
from ttpd.FetchHandler import FetchHandler
from ttpd.Package import Package
import config

class TTPDProtocol:
    
    def __init__(self):
        pass

    def resolve(self, package: Package) -> CommandHandler:
        match package.method:
            case config.FETCH:
                return FetchHandler(package)
            case config.CHECK:
                return CheckHandler(package)
            case _:
                return ErrorHandler(package)
