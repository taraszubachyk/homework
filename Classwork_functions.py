print("---------------------------TASK 1-----------------------------")
# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.
def average_of_numbers (*args):
    return sum(args)/len(args)
print ("Середнє  арифметичне: ", average_of_numbers(1,15,654,44,5256,74))

print("---------------------------TASK 2-----------------------------")
# 2.  Написати функцію, яка повертає абсолютне значення числа
def absolute_number (num):
    return abs(num)
print(absolute_number(-25))

print("---------------------------TASK 3-----------------------------")
# 3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.
def finding_maximum_of_two (x,y):
    return max(x,y)
print(finding_maximum_of_two(34,23))

print("---------------------------TASK 4-----------------------------")
# 4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
def area_of_the_rectangle (x,y):
    return x*y
def area_of_the_triangle (a,b):
    return 0.5 * a*b
def area_of_the_circle (r):
    return 3.14 * (r**2)

task = int(input("Площу якої фігури ви хочете обчислити Прямокутник - 1, Трикутник - 2, Коло - 3: "))
if task == 1:
    x = float(input("Сторона A: "))
    y = float(input("Сторона В: "))
    area = area_of_the_rectangle(x,y)
    print("Площа прямокутника: ", area)

elif task == 2:
    x = float(input("Катет A: "))
    y = float(input("Катет В: "))
    area = area_of_the_triangle(x,y)
    print("Площа трикутнкика: ", area)

elif task == 3:
    r = float(input("Раріус кола: "))
    area = area_of_the_circle(r)
    print("Площа кола: ", area)

print("---------------------------TASK 5-----------------------------")
# 5.  Написати функцію, яка обчислює суму цифр введеного числа.
def sum_of_numbers (x):
    convertation = list(x)
    new_number_list =[]
    for i in convertation:
        i = float(i)
        new_number_list.append(i)
    return sum(new_number_list)
number = input("Введіть число: ")
print(sum_of_numbers(number))



print("---------------------------TASK 6-----------------------------")
# 6.  Написати програму калькулятор, яка складається з наступних функцій:
# головної, яка пропонує вибрати дію та додаткових,
# які реалізовують вибрані дії, калькулятор працює доти,
# поки ми не виберемо дію вийти з калькулятора, після виходу,
# користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

def addition (x,y):
    return x+y
def subtraction (x,y):
    return x-y
def multiplication (x,y):
    return x*y
def devision (x,y):
    return x/y


while True:
    task = input("Яку дію ви хочете виконати? + - * / :\nДля вихoду введіть  Exit:  ")
    if task == "Exit":
        print("Дякую за вибір нашого програмного продукту")
        break
    elif task == "+":
        num_1 = float(input("Введіть 1 число: "))
        num_2 = float(input("Введіть 2 число: "))
        print(addition(num_1,num_2))
    elif task == "-":
        num_1 = float(input("Введіть 1 число: "))
        num_2 = float(input("Введіть 2 число: "))
        print(subtraction(num_1,num_2))
    elif task == "*":
        num_1 = float(input("Введіть 1 число: "))
        num_2 = float(input("Введіть 2 число: "))
        print(multiplication(num_1,num_2))
    elif task == "/":
        num_1 = float(input("Введіть 1 число: "))
        num_2 = float(input("Введіть 2 число: "))
        print(devision(num_1,num_2))

    else:
        print("Введено  невірну дію над  числами")







