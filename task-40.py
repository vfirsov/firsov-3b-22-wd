import os

check_file = os.path.isfile('text.txt')

if check_file:
    print('Файл существует')
else:
    print('Файл не существует')
