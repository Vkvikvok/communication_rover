#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
import socket
from example_interfaces.srv import SendGoal # Buraya bir tane service tipi girilecek

class Send_Goal_Client_Node(Node):
    def __init__(self):
        super().__init__("send_goal_client")

    def call_communication_server(self, location):
        client = self.create_client(SendGoal, "send_goal")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Send Goal...")
        
        request = SendGoal.Request()
        request.location = location #Kullanıcıdan alınan konum bilgisi buraya girilecek

        future = client.call_async(request)
        future.add_done_callback(self.callback_call_send_goal)

    def callback_call_send_goal(self, future):
        try:
            response = future.result()
            if response.success == 1:
                self.get_logger().info("Sending goal is successfull")
            else:
                self.get_logger().info("Sending goal is failed")

        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))    
        
    try:
        #Socket örneği oluşturuldu(IPv4, UDP, sürekli bağlantıyı kontrol edecek şekilde ayarlandı)
        sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        #Socket sunucuya bağlanacak
        sock_client.bind(("192.168.1.10", 22))

        #Veri yolla
        data = "".encode("utf-8")#encode edilmiş gps verisi
        sock_client.send(data)

        #Socket kapatıldı
        sock_client.close()

    except socket.error as e:
        # Bağlantı kurulamadı!
        print(f'Bağlantı kurulamadı: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = Send_Goal_Client_Node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()