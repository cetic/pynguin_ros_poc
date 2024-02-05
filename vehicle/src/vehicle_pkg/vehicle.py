from rclpy.node import Node
from rclpy import init, spin

DEFAULT_POLICY = 50


class Vehicle(Node):

    shape: str
    speed_policy: int

    def __init__(self, *args, **kwargs):
        super().__init__('vehicle', *args, **kwargs)
        self.speed_policy = DEFAULT_POLICY
        self.set_shape(1,1,1)
        self.get_logger().info('Vehicle node Created')

    def set_shape(self, x: int, y: int, z: int) -> None:
        # trying to use the quickstart Pynguin example
        if x == y == z:
            self.shape = "Equilateral triangle"
        elif x == y or y == z or x == z:
            self.shape = "Isosceles triangle"
        else:
            self.shape = "Scalene triangle"


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
