import socket
import struct

listen_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('0.0.0.0', listen_port))

data, client_address = server_socket.recvfrom(16)

(latitude, longitude, yaw, roll) = struct.unpack('!ffff', data)

server_socket.close()
