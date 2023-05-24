idea from https://medium.com/swlh/raspberry-pi-ros-2-camera-eef8f8b94304

needed for compile:

git clone --branch humble https://gitlab.com/boldhearts/ros2_v4l2_camera.git


ros2 run v4l2_camera v4l2_camera_node

ros2 run py_image_flip image_flip node

rosdep install --from-paths src -r -y
