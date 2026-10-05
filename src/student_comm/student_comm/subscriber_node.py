import rclpy
from rclpy.node import Node
from student_info_interfaces.msg import StudentInfo
class StudentInfoSubscriber(Node):
    def __init__(self):
        super().__init__("student_info_subscriber") 
        self.subscription_=self.create_subscription(
            StudentInfo,
            "student_info",
            self.listener_callback,
            10
        )
        self.get_logger().info("subscribing,waiting")


    def listener_callback(self,msg):
        self.get_logger().info(f'姓名:{msg.student_name},学号:{msg.student_id},专业:{msg.student_major}')
    
def main(args=None):
    rclpy.init(args=args)
    node=StudentInfoSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass   
    finally:
        print("我不是奶龙")
        node.destroy_node() 
        if rclpy.ok():
            rclpy.shutdown()
        
if __name__ =="__main__":
    main()
         
         
