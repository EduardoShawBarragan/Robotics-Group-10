import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class StationaryRobotScan(Node):
    def __init__(self):
        super().__init__('stationary_robot_scan')
        self.camera_sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.camera_callback,
            10
        )
        self.bridge = CvBridge()
        self.get_logger().info("Stationary scanning robot node started.")

    def camera_callback(self, msg):
        # Convert the ROS Image message to an OpenCV image
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        
        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define red color range in HSV
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        
        # Create a mask for red color
        mask = cv2.inRange(hsv, lower_red, upper_red)
        
        # Count non-zero pixels in the mask (i.e., red pixels)
        red_pixels = cv2.countNonZero(mask)

        if red_pixels > 0:
            self.get_logger().info("Red cube detected!")
        else:
            self.get_logger().info("Scanning for red cube...")

def main(args=None):
    rclpy.init(args=args)
    node = StationaryRobotScan()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
