#Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

x=11
y=22

y = x + y
x = (x - y) * (-1)
y = y - x
print(x, y)