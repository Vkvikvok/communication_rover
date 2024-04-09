import socket
import struct

server_ip = '127.0.0.1'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))
yaw = float(input("Enter yaw: "))
roll = float(input("Enter roll: "))

try:
    data = struct.pack('!ffff', latitude, longitude, yaw, roll)

    client_socket.sendto(data, (server_ip, server_port))

except Exception as e:
    print(-1)

finally:
    client_socket.close()
