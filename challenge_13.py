class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width + self.length

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    def change_size(self, c):
        self.width += c
        self.length += c

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

rectangle = Rectangle(5, 3)
square = Square(4, 4)

print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())

square.change_size(5)
print(square.calculate_perimeter())

square.change_size(-1)
print(square.calculate_perimeter())

square.what_am_i()

mick = Rider("Mick Jagger")
stan = Horse("Stanley", mick)
print(stan.rider.name)
