import socket
import time
from config import HOST, PORT, BUFFER_SIZE, SUCCESS_CODE
from utils import build_package

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (HOST, PORT)

while True:
    message = "FETCH test_file.txt".encode()
    sock.sendto(build_package(0, message, SUCCESS_CODE), server_address)

    data, addr = sock.recvfrom(BUFFER_SIZE)
    print('Received:', data.decode())

    time.sleep(5)

sock.close()
