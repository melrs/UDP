import socket
from config import BUFFER_SIZE

def fetch(filename):
    try:
        with open(filename, 'rb') as file:
            while True:
                chunk = file.read(BUFFER_SIZE)
                if not chunk:
                    break
                yield chunk
    except FileNotFoundError:
        yield "ERROR - File not found".encode()

def check(filename):
    try:
        with open(filename, 'rb'):
            yield "File exists".encode()
    except FileNotFoundError:
        yield "ERROR - File not found".encode()

def handle_request(data):
    request = data.decode()
    command, filename = request.split(maxsplit=1)

    match command:
        case 'FETCH':
            return fetch(filename)
        case 'CHECK':
            return check(filename)
        case _:
            return iter(["ERROR - Invalid command".encode()])