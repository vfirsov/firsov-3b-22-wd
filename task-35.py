a = 1
b = 1

n = int(input("Фибоначи номер: "))

i = 0
while i < n - 2:
    summ = a + b
    a = b
    b = summ
    i = i + 1

print("Значение:", b)
