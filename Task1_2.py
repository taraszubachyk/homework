#Задано чотирицифрове натуральне число.
#Знайти добуток цифр цього числа.
#Записати число в реверсному порядку.
#Посортувати цифри, що входять в дане число

natural_number =input("Веддіть чотирицифрове натуальне число: ")

char1 = int (natural_number[0])
char2 = int (natural_number[1])
char3 = int (natural_number[2])
char4 = int (natural_number[3])

multiplication = char1*char2*char3*char4
print("Добуток цифр: ", multiplication)

reversed_number = natural_number[::-1]
print("Число в реверсивному порядку: ", reversed_number)

sorted_nubmer =''.join(sorted(natural_number))
print("Посортовані цифри заданого  числа: ", sorted_nubmer)