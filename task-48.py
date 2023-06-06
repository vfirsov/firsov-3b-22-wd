list = [5, 7, 11, 13, 15, 20, 25]

result = 0
counter = 0
MAGIC_VALUE = 10

for item in list:
    if item > MAGIC_VALUE:
        result += item
        counter += 1

print(result/counter)
