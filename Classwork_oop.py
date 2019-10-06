print("---------------------------TASK 1-----------------------------")
# Створити батьківський клас Figure з методами init: ініціалізується колір,
# get_color: повертає колір фігури,
# info: надає інформацію про фігуру та колір,
# від якого наслідуються такі класи як Rectangle, Square,
# які мають інформацію про ширину, висоту фігури, метод square,
# який знаходить площу фігури.

class Figure:
    def __init__(self,color):
        self.color = color
    def get_color(self):
        return print(self.color)
    def info(self):
        return print( f"Figure is {self.color} color")
    def area(self):
        return self.width * self.height
class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height
class Square(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

c1 = Rectangle(12,23,"red")


