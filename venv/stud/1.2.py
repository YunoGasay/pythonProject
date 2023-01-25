import math
a = int(input('a = '))
b = int(input('b = '))
mat = int(input('Выберете номер действия: 1- сумма, 2- вычитание, 3- деление, 4-умножение'))
if mat == 1:
    print(a + b)
elif mat == 2:
    print(a - b)
elif mat == 3:
    print(a / b)
elif mat == 4:
    print(a * b)
else:
    print('нет такого действия')

input('второй вариант задания')
a = int(input('a = '))
b = int(input('b = '))
a = a + b
b = a * b
a = b / a
b = b - a
print('a = ',a)
print('b = ',b)