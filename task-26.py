def find_nok(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print((a + b))


userNumber_1 = int(input('Введите число 1:'))
userNumber_2 = int(input('Введите число 2:'))

find_nok(userNumber_1, userNumber_2)
