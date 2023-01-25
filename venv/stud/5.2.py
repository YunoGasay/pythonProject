def sist():
    n = int(input('Введите число n:'))
    a = ''
    while n > 0:
        a = str(n % 2) + a
        n //= 2
    print('Число в двоичной системе счисления:',a)
sist()