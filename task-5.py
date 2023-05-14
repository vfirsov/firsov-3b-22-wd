exclude = {
    4: True,
    7: True
}

for x in range(1, 11):
    if exclude.get(x):
        continue
    print(x)

