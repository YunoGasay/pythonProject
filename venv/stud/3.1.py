x = int(input('Введите число:'))
s = 0
while x != -1:
    s = s + x
    x = int(input('Введите новое число:'))
print('Сумма равна:',s)