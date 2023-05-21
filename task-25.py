def is_simple(number):
    for i in range(2, number):
        if (number % i) == 0:
            return print('не простое')
    return print('простое')


userNumber = int(input('Введите число'))
is_simple(userNumber)
