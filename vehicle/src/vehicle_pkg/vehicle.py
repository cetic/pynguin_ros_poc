from rclpy.node import Node
from rclpy import init, spin

from std_msgs.msg import String
from random import randrange

DEFAULT_POLICY = 50

class Vehicle(Node):

    policy: int

    def __init__(self, *args, **kwargs):
        super().__init__('vehicle', *args, **kwargs)
        self.get_logger().info('Vehicle node Created')
        self.publisher_ = self.create_publisher(String, 'vehicle_logs', 10)

        # Listen to vehicle policy
        self.subscription = self.create_subscription(
            String,
            'vehicle_policy',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.policy = DEFAULT_POLICY

    def update_policy(self, policy):
        self.policy = policy
        msg = String()
        msg.data = policy
        self.publisher_.publish(msg)
        self.get_logger().info('Changed speed to: "%s"kph' % msg.data)

    def listener_callback(self, msg):
        self.get_logger().info('Received new policy: "%s"kph' % msg.data)
        new_speed = msg.data
        self.update_policy(new_speed)

    def get_speed(self) -> float:
        # simulate speed close to policy
        return max(0, randrange(self.policy-5, self.policy))

def main():
    init(args=None)
    vehicle = Vehicle()
    spin(vehicle)
    try:
        vehicle()
    except Exception as exception:  
        pass

if __name__ == '__main__':
    main()
