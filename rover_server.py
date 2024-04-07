#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
import socket

from example_interfaces.srv import SendGoal #Buradaki service dosyasının çekildiği paket değiştirilecek

class SendGoalServerNode(Node):
    def __init__(self):
        super().__init__("send_goal_server")
        self.server_ = self.create




try:
    #Socket örneği oluşturuldu(IPv4, UDP, sürekli bağlantıyı kontrol edecek şekilde ayarlandı)
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 
                        socket.SO_KEEPALIVE)

    #Socket sunucuya bağlanacak
    sock_server.bind(("192.168.1.11", 22))

    #Gelen bağlantıları dinlemek için soketi hazırla (en fazla 5 bağlantı bekleyebilir)
    sock_server.listen(1)

    #Sunucudan gelen bağlantıyı kabul et
    conn, add = sock_server.accept()

    while True:

        #PC den gelen gps verisini alacak
        data = sock_server.recv(1024).decode("utf-8") #1024 byte veri alacak

    #Socket kapatıldı
    sock_server.close()

except socket.error as e:
    # Bağlantı kurulamadı!
    print(f'Bağlantı kurulamadı: {e}')



def main(args=None):
    rclpy.init(args=args)
    node = SendGoalServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()