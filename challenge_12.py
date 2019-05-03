import math

class Apple:
    def __init__(self, w, s, c, v):
        self.weight = w
        self.size = s
        self.color = c
        self.variety =v

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi

class Triangle:
    def __init__(self, h, b):
        self.height = h
        self.bottom =b

    def area(self):
        return self.bottom * self.height / 2

class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

circle = Circle(10)
print(circle.area())

triangle = Triangle(10, 20)
print(triangle.area())

hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())
