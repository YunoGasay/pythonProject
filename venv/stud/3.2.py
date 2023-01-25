x = int(input('Введите число:'))
i = x%10
x = x//10
while x > 0 :
    if x%10 > i:
        i = x%10
    x = x//10
print(i)
