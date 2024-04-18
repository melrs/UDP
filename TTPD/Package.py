import json

class Package:

    def __init__(self, package_id, status_code, size, data, checksum, method):
        self.package_id = package_id
        self.status_code = status_code
        self.size = size
        self.data = data
        self.checksum = checksum
        self.method = method
    
    def encode(self):
        return json.dumps({
            "package_id": self.package_id,
            "status_code": self.status_code,
            "size": self.size,
            "data": self.data.decode(),
            "checksum": self.checksum,
            "method": self.method
        }).encode()
    
    @staticmethod
    def decode(data):
        package = json.loads(data.decode())
        return Package(package["package_id"], package["status_code"], package["size"], package["data"].encode(), package["checksum"], package["method"])
