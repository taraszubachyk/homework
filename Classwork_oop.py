print("---------------------------TASK 1-----------------------------")
# Створити батьківський клас Figure з методами init: ініціалізується колір,
# get_color: повертає колір фігури,
# info: надає інформацію про фігуру та колір,
# від якого наслідуються такі класи як Rectangle, Square,
# які мають інформацію про ширину, висоту фігури, метод square,
# який знаходить площу фігури.

class Figure:
    def __init__(self,color):
        self.get_color = color
        self = self
    # def __repr__(self):
    #     return f"{self}"
    def info(self):
        return print( f"This is {self.get_color} ")

class Square(Figure, width, high):

    def square(self,a,b):
        return print(a*b)
class Rectangle(Figure):
    pass

c1 = Square()