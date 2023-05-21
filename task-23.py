x = int(input('число'))

a = [1, 4, 6, 8]

for i in a:
    if i == x:
        print('число найденно в массиве')
        exit()
    else:
        print('число не найдено в массиве')
        exit()

