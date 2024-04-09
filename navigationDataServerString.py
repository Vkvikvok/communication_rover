import socket
import struct

server_ip = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

navigation_data = input(":")

try:
    data = struct.pack(f'!{len(navigation_data)}s', navigation_data.encode())

    server_socket.sendto(data, (server_ip, server_port))

except Exception as e:
    print(-1)

finally:
    server_socket.close()
