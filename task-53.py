arr = [1, 2, 3, 2, 1]
arrReverse = reversed(arr)

# print(str(arr1))
arrAsStr = str(arr)

arr.reverse()

arrReverseAsStr = str(arr)

if arrAsStr == arrReverseAsStr:
    print('Это палиндром')
else:
    print('Это не палиндром')
