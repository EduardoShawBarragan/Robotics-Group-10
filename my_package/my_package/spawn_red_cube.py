import rclpy
from rclpy.node import Node
import random
from webots_ros2_msgs.srv import SpawnNode

class CubeSpawnerNode(Node):
    def __init__(self):
        super().__init__('cube_spawner')
        # Create a service to spawn the red cube
        self.spawn_service = self.create_service(SpawnNode, 'spawn_red_cube', self.spawn_red_cube_callback)

    def spawn_red_cube_callback(self, request, response):
        # Generate random coordinates within defined bounds
        x = random.uniform(-1, 1)  # Adjust these as needed for your world
        y = 0.05  # Small height to place on ground level
        z = random.uniform(-1, 1)

        # Prepare the spawn service request
        spawn_request = SpawnNode.Request()
        spawn_request.node_name = 'RED_CUBE'
        spawn_request.node_type = 'Solid'  # Set type as needed
        spawn_request.translation = [x, y, z]
        spawn_request.rotation = [0, 1, 0, 0]  # No rotation

        # Call the service to spawn the red cube
        future = self.spawn_service.call_async(spawn_request)
        rclpy.spin_until_future_complete(self, future)

        if future.result().success:
            response.success = True
            response.message = f"Red cube spawned at random location: x={x}, y={y}, z={z}"
        else:
            response.success = False
            response.message = "Failed to spawn red cube"

        return response

def main(args=None):
    rclpy.init(args=args)
    cube_spawner = CubeSpawnerNode()
    rclpy.spin(cube_spawner)
    cube_spawner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
