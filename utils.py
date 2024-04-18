import hashlib
import socket

def calculate_checksum(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def receive_all_from_socket(server_socket: socket.socket, buffer_size: int):
    data = b""
    while True:
        part, addr = server_socket.recvfrom(buffer_size)
        data += part
        print('Received:', part.decode())
        if len(part) < buffer_size:
            break
    return [data, addr]