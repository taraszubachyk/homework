print("---------------------------TASK 1-----------------------------")
# 1.  Роздрукувати всі парні числа менші 100 (написати два варіанти коду:
# один використовуючи цикл while, а інший з використанням циклу for).

for i in range (1,100):
    if i%2 == 0:
        print(i,end =" ")
print(" ")

for i in range (0,100,2):
    if i == 0:
       continue
    print(i,end =" ")

print(" ")

i = 0
while i < 98:
    i +=2
    print(i,end =" ")
print(" ")

i = 1
while i < 100:
    if i%2 == 0:
        print(i,end =" ")
    i = i+1
print(" ")


print("---------------------------TASK 2-----------------------------")
# 2.  Роздрукувати всі непарні числа менші 100.
# (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).

for i in range(1,100):
    if i%2!=0:
     print(i,end =" ")
print(" ")

for i in range(100):
    if i%2==0:
        continue
    print(i,end =" ")
print(" ")


print("---------------------------TASK 3-----------------------------")
# 3.  Перевірити чи список містить непарні числа.
#           (Підказка: використати оператор break)


some_numberlist = [12,456,543,23,456,457,89,944]

for number in some_numberlist:
    if number%2!=0:
        print("Є непарні")
        break
print("---------------------------TASK 4-----------------------------")
# 4.  Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою.
# (Підказка: використати вбудовану функцію float ()).

some_numberlist = [12,456,543,23,456,457,89,944]
new_l = []
for i in some_numberlist:
    i = float(i)
    new_l.append(i)
print(new_l)

print("---------------------------TASK 5-----------------------------")
# 5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

# fib1=1
# fib2=1
# n=30
# spys = []
# while fib1 < n:
#     fib1,fib2 = fib1,fib1+fib2
#     spys.append(fib1)
# print(spys)

print("---------------------------TASK 6-----------------------------")
#6.  Створити список, що складається з чотирьох елементів типу string. Потім, за допомогою циклу for, вивести елементи по черзі на екран.

some_list = ["Taras","Lviv","28","2019"]

for i in some_list:
    print(i)

print("---------------------------TASK 7-----------------------------")
# 7.  Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”.
#           (Підказка: цикл for може бути вкладений в інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).

for i in some_list:
    for i in i:
        i += "%"
        print(i, end=" ")
print(" ")
print("---------------------------TASK 8-----------------------------")
#8.  Юзер вводить число з клавіатури, написати скріпт, який визначає чи це число просте чи складне.

number = input("Введіть число: ")

