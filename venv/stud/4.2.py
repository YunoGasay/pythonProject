n = int(input('Введите число n:'))
s = 0
for i in range(1,n+1):
    a = 1
    for j in range(1,i+1):
        a *= j
    s += a
print(s)
