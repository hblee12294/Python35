L = [x * x for x in range(1, 11)]
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

import os
print([d for d in os.listdir('.')])

L = ["Hello", "World", "IBM", "Apple"]
print([s.lower() for s in L])