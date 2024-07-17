#! /usr/bin/env python
import rclpy
from rclpy.node import Node

class My_Node(Node):
    def __init__(self):
        super().__init__("my_node")
        self.get_logger().info("The Node has started now ")
        self.create_timer(1,self.timer_cb)
        self.counter=0
    def timer_cb(self):
        self.counter+=1
        self.get_logger().info("Hello World "+str(self.counter))

def main(args=None):
    rclpy.init(args=args)
    node =My_Node()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__=='__main__':
    main()