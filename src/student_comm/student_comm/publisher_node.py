import rclpy
from rclpy.node import Node
from student_info_interfaces.msg import StudentInfo
class StudentInfoPublisher(Node):
    X="xttbwm"
    Y="665710086"
    def  __init__(self):
        super().__init__("student_info_publisher")
        self.publisher_=self.create_publisher(StudentInfo,"student_info",10)
        self.timer_=self.create_timer(1,self.timer_callback)
        self.count=0
        self.get_logger().info("每1s发布一次")


    def timer_callback(self):
        msg=StudentInfo()
        msg.student_id=self.Y
        msg.student_name=self.X
        self.publisher_.publish(msg)
        self.count+=1
        self.get_logger().info(f'{self.count},{msg.student_id},{msg.student_name}')


def main(args=None):
    rclpy.init(args=args)
    node=StudentInfoPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("ctrl+c,quit now")
    finally:
    	node.destroy_node()
    	if rclpy.ok():
            rclpy.shutdown()


if __name__ =="__main__":
    main()
