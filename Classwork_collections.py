print("---------------------------TASK 1-----------------------------")
# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

spysok= []

while True:
 numbers = input("Введіть ціле число: ")
 if numbers=="":
     break
 numbers = int (numbers)
 spysok.append(numbers)

print(spysok)

max_number = max(spysok)
min_number = min(spysok)
print("Max number is: ", max_number)
print("Min number is: ", min_number)

print("---------------------------TASK 2-----------------------------")
# 2.  В інтервалі від 1 до 10 визначити числа
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3,
# •  числа, які не діляться на 2 та 3.

for i  in range(1,10):
    if i%2==0:
        print( i, end = " ")
    elif i%3==0:
        print(i, end = " ")
    elif i%2!=0 and i%3!=0:
        print(i, end = " ")


print(" ")

print("---------------------------TASK 3-----------------------------")
#3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)
number = int (input("Введіть ціле число: "))
result = 1
for i in range(1,number):
    result = result*(i+1)
print(result)



print("---------------------------TASK 4-----------------------------")
# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач.
# Якщо логін вірний (First), то привітайте користувача.
# Якщо ні, то виведіть повідомлення про помилку.
# (використайте цикл while)

login = "First"

login_vvid = input("Enter your login: ")

# def login_check (login):
#     if login == "First":
#         print("Congrats")
#     else:
#         print("Invalid login")
# login_check(login_vvid)

if login_vvid == "First":
    print("Congrats")
while login_vvid != "First":
    print("Invalid login")
    break
