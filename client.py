import socket
import time
import config
from utils import build_package

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (config.HOST, config.PORT)

while True:
    message = "test_file.txt".encode()
    sock.sendto(build_package(0, message, config.SUCCESS_CODE, config.FETCH), server_address)

    data, addr = sock.recvfrom(config.BUFFER_SIZE)
    print('Received:', data.decode())

    time.sleep(5)

sock.close()
