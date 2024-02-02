from rclpy.node import Node
from rclpy import init, spin

DEFAULT_POLICY = 50


class Vehicle(Node):

    shape: str

    def __init__(self, *args, **kwargs):
        super().__init__('vehicle', *args, **kwargs)
        self.get_logger().info('Vehicle node Created')

    def triangle(self, x: int, y: int, z: int) -> str:
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
