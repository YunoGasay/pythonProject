h = int(input('Введите высоту:'))
n = str(input('Введите символ:'))
for i in range (h):
    print(f"{' ' * ( h - i ) } { n * i } || { n * i }")
print(' ' * h + '  ||  ')