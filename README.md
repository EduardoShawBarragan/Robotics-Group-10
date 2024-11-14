# Robotics-Group-10

How to install webots:

Linux:
sudo apt-get install ros-jazzy-webots-ros2

I would recommend using Linux, but it may work in Windows and MacOS
Windows: https://docs.ros.org/en/jazzy/Tutorials/Advanced/Simulators/Webots/Installation-Windows.html
MacOS: https://docs.ros.org/en/jazzy/Tutorials/Advanced/Simulators/Webots/Installation-MacOS.html

How to run the code:

go to:
.../Robotics-Group-10

then run:
source install/local_setup.bash
ros2 launch my_package robot_launch.py

on a second terminal run:
ros2 topic pub /cmd_vel geometry_msgs/Twist  "linear: { x: 0.1 }"


When you make changes to the code, you need to run this before running the code the same way as above:
colcon build

