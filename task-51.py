import math
from functools import reduce

arr1 = [24, 36, 48, 60]
arr2 = [12, 18, 24, 36, 72]

nok1 = reduce(math.gcd, arr1)
nok2 = reduce(math.gcd, arr2)

print(math.gcd(nok1, nok2))
