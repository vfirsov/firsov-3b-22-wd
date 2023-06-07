import math

pointers = [(1, 2), (3, 4), (-1, 5), (6, -3)]

pointers.sort(key=lambda a: math.dist((0, a[0]), (0, a[1])))

print(pointers)

