import hashlib
import socket
import config

from ttpd.Package import Package

def calculate_checksum(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def build_package(id: int, data, status_code: int, method: str = config.SEND):
    return Package(id, status_code, len(data), data, calculate_checksum(data), method).encode()