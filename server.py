from UDP.UDPServer import UDPServer
from commons.config import BUFFER_SIZE, HOST, PORT


server = UDPServer(HOST, PORT, BUFFER_SIZE)
server.start()