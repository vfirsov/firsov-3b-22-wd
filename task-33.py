string = input('string ')
stringMap = set(string)

for i in stringMap:
    i_counter = 0

    for j in string:
        if i == j:
            i_counter += 1

    print(i, i_counter)



