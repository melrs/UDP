import socket
import json
import commons.config as config
from commons.utils import build_package, calculate_checksum

ids_to_recover = []
received_data = []
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (config.HOST, config.PORT)
filename = input("Enter the file name: ")

def get_file_name():
    if not ids_to_recover:
        return filename.encode()
    
    return (filename+' '+(' '.join(map(str, ids_to_recover)))).encode()

def receive_data(sock, server_address):
    while True:
        data, addr = sock.recvfrom(config.BUFFER_SIZE)
        data = json.loads(data.decode())
        if data['status_code'] == config.SUCCESS_CODE:
            break
        
        discard = input("Do you want to discard this part of the file? (y/n): ")
        if discard.lower() == 'y':
            if data['package_id'] not in ids_to_recover:
                ids_to_recover.append(data['package_id'])
            continue

        received_data.insert(data['package_id'], data)

while True:
    sock.sendto(build_package(0, get_file_name(), config.SUCCESS_CODE, config.FETCH), server_address)
    receive_data(sock, server_address)

    print(ids_to_recover)
    for data in received_data:
        if data['package_id'] in ids_to_recover and data['checksum'] == calculate_checksum(data['data'].encode()):
            ids_to_recover.remove(data['package_id'])
            print(f"Package {data['package_id']} received successfully!")

    if not ids_to_recover:
        print("All data received successfully!")
        break


sorted_data = sorted(received_data, key=lambda x: x['package_id'])
print("Writing file...")
with open('received_'+filename, 'wb') as file:
    for data in sorted_data:
        file.write(data['data'].encode())
        
file.close()
sock.close()