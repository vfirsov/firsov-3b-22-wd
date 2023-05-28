try:
    num = int(input('ВВедите число '))
    print(num*num)

except ValueError:
    print('Error')
    quit()
