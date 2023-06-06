try:
    c = str(input('Введите список целых чисел: '))
    c_list = c.split(',')
    minn = int(c_list[0])

    for i in range(0, len(c_list)):
        item = int(c_list[i])

        if item < minn:
            minn = item

    print(minn)

except ValueError:
    print('Error')
    quit()
