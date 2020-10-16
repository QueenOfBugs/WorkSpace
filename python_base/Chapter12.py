# programming paradigm

# object-oriented programming paradigm

# challenge 12.6

import math


class Apple:
    def __init__(self, color, weight, stem_length, circumference):
        self.color = color
        self.weight = weight
        self.stem_length = stem_length
        self.circumference = circumference


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi


class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6


if __name__ == '__main__':
    hexagon = Hexagon(3, 2, 1, 4, 3, 3)
    print(hexagon.calculate_perimeter())

    triangle = Triangle(3, 4)
    print(triangle.area())

    circle = Circle(2)
    print(circle.area())
