try:
    n = int(input('Введите число n: '))
    summ = 0

    for i in range(1, n+1):
        summ += i

    print(summ)

except ValueError:
    print('Error')
    quit()
