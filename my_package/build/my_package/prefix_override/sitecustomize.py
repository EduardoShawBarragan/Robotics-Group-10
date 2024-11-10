import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/eduardo/Desktop/assignment/Robotics-Group-10/my_package/install/my_package'
