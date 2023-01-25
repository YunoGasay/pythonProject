a = int(input('Введите число А:'))
b = int(input('Введите число B:'))
if a < b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
