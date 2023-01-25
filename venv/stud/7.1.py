file = open('Список студентов.txt.txt','w')
f = str(input('Введите фамилию студента и его почтовый адрес: '))
with open('Список студентов.txt.txt','w') as f2:
    f2.write(f'{f}\n')
d = str(input('Ввести ещё данные?: '))
while d == 'Да' or d == 'да':
    f = str(input('Введите фамилию студента и его почтовый адрес:'))
    with open('Список студентов.txt.txt', 'a') as f2:
        f2.write(f'{f}\n')
    d = str(input('Ввести ещё данные?:'))
file.close()