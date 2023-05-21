string = input('строка')
n = len(string)
new_string = ''

while n > 0:
    new_string += string[n-1]
    n -= 1

print(new_string)
