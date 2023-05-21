o = input('operation (pls, mns, mul, div)')

if o in ('pls', 'mns', 'mul', 'div'):
    a = int(input('a'))
    b = int(input('b'))

    if o == 'pls':
        print(a+b)

    if o == 'mns':
        print(a-b)

    if o == 'mul':
        print(a*b)

    if o == 'div':
        print(a/b)
