import random

result = []
i = 0
minNum = 0
maxNum = 0

while i < 10:
    num = random.randint(0, 100)
    result.append(num)

    if num < minNum:
        minNum = num

    if num > maxNum:
        maxNum = num

    i += 1


print(minNum, maxNum)

