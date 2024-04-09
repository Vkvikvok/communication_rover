import socket
import struct

listen_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.bind(('144.122.4.143', listen_port))

data, client_address = client_socket.recvfrom(1024)

navigation_data = struct.unpack(f'!{len(data)}s', data)[0].decode()

client_socket.close()
