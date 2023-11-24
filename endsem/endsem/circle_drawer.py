import rclpy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class CircleDrawer:
    def __init__(self, node):
        self.node = node
        self.turtle_publisher = node.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = node.create_timer(0.1, self.timer_callback)  # Adjust the timer duration as needed

        # Initial movement command
        self.move_cmd = Twist()
        self.move_cmd.angular.z = 1.0  # Initial angular speed
        self.move_cmd.linear.x = 1.0  # Initial linear speed

    def timer_callback(self):
        self.turtle_publisher.publish(self.move_cmd)

    def draw_circle(self):
        rclpy.spin(self.node)

def main():
    rclpy.init()

    node = rclpy.create_node('circle_drawer')
    circle_drawer = CircleDrawer(node)

    # Draw a circle
    circle_drawer.draw_circle()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

