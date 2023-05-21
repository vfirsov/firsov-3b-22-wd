import random

result = []
i = 0
summ = 0

while i < 10:
    num = random.randint(0, 10)
    result.append(num)
    i += 1
    summ += num


print(result, summ)

