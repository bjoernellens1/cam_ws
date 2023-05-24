#!/usr/bin/env python3

import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageFlip(Node):
    def __init__(self):
        super().__init__('image_flip_node')
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',  # Replace 'camera_topic' with the actual camera topic name
            self.image_callback,
            10  # Adjust the queue size as needed
        )
        self.publisher = self.create_publisher(
            Image,
            'image_raw_flipped',  # Replace 'flipped_camera_topic' with the desired output topic name
            10  # Adjust the queue size as needed
        )
        self.cv_bridge = CvBridge()

    def image_callback(self, msg):
        # Convert ROS Image message to OpenCV image
        cv_image = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Flip the image
        flipped_image = cv2.flip(cv_image, 0)

        # Convert OpenCV image back to ROS Image message
        flipped_msg = self.cv_bridge.cv2_to_imgmsg(flipped_image)

        # Publish the flipped image
        self.publisher.publish(flipped_msg)


def main(args=None):
    rclpy.init(args=args)
    image_flipper_node = ImageFlip()
    rclpy.spin(image_flipper_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


