import functools

int2 = functools.partial(int, base = 2)

print("100000 =", int2("100000"))
print("101010 =", int2("101010"))
print("101010 =", int2("101010", base = 10))