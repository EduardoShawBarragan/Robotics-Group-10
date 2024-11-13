from controller import Supervisor
import rclpy
from rclpy.node import Node
from webots_ros2_msgs.srv import SpawnNode

class WebotsSupervisor(Supervisor):
    def __init__(self):
        super().__init__()
        rclpy.init()
        self.node = Node('webots_supervisor')
        self.node.create_service(SpawnNode, 'spawn_red_cube', self.spawn_red_cube)

    def spawn_red_cube(self, request, response):
        # Create the cube at the specified random position
        cube = self.getFromDef("RED_CUBE")
        if cube is None:
            cube = self.getRoot().getField('children').importMFNodeFromString(-1, 'DEF RED_CUBE Solid { translation ' + ' '.join(map(str, request.translation)) + ' appearance PBRAppearance { baseColor 1 0 0 } }')
        else:
            cube.getField("translation").setSFVec3f(request.translation)

        response.success = True
        response.message = "Red cube spawned"
        return response

    def run(self):
        while self.step(int(self.getBasicTimeStep())) != -1:
            rclpy.spin_once(self.node)

if __name__ == '__main__':
    supervisor = WebotsSupervisor()
    supervisor.run()
