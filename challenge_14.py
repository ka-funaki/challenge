class Square:
    square_list = []
    
    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    def print_size(self):
        print("{} by {} by {} by {}".format(self.side, self.side, self.side, self.side))

s1 = Square(29)
print(s1.square_list)
s1.print_size()

def input_two_parameter(x1, x2):
    print(x1 is x2)

input_two_parameter(1, 2)
input_two_parameter(1, 1)
