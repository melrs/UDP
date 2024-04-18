from TTPD.CheckHandler import CheckHandler
from TTPD.CommandHandler import CommandHandler
from TTPD.ErrorHandler import ErrorHandler
from TTPD.FetchHandler import FetchHandler
from TTPD.Package import Package
import commons.config as config

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
