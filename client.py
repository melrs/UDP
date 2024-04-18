import socket
import json
import config
from utils import build_package, calculate_checksum

ids_to_recover = []
received_data = []
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (config.HOST, config.PORT)
filename = input("Enter the file name: ")

def get_file_name():
    if not ids_to_recover:
        return filename.encode()
    
    return (filename+' '+(', '.join(map(str, ids_to_recover)))).encode()

def receive_data(sock, server_address):
    while True:
        data, addr = sock.recvfrom(config.BUFFER_SIZE)
        data = json.loads(data.decode())
        if data['status_code'] == config.SUCCESS_CODE:
            break
        
        print(f"Received package {data['data']}")
        discard = input("Do you want to discard this part of the file? (y/n): ")
        if discard.lower() == 'y':
            data['data'] = ''


        if data in received_data : received_data.pop(data['package_id'])
        received_data.insert(data['package_id'], data)

while True:
    sock.sendto(build_package(0, get_file_name(), config.SUCCESS_CODE, config.FETCH), server_address)
    receive_data(sock, server_address)
    ids_to_recover = []
    print(received_data)
    for data in received_data:
        if data['checksum'] != calculate_checksum(data['data'].encode()):
            ids_to_recover.append(data['package_id'])

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