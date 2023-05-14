class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y


first_rectangle = Rectangle(10, 20)

print(first_rectangle.get_area())
