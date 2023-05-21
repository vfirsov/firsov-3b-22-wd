from calculator import pls, mns, mul, div

o = input('operation (pls, mns, mul, div)')

if o in ('pls', 'mns', 'mul', 'div'):
    a = int(input('a'))
    b = int(input('b'))

    if o == 'pls':
        print(pls(a, b))

    if o == 'mns':
        print(mns(a, b))

    if o == 'mul':
        print(mul(a, b))

    if o == 'div':
        print(div(a, b))
