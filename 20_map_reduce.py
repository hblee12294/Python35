def f(x):
	return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7])
print(list(r))

print()
print(list(map(str, [1, 2, 3, 4, 5, 6])))

from functools import reduce

def add(x, y):
	return x + y

print()
print(reduce(add, [1, 3, 5, 7, 9]))

# practice 1
def normalize(name):
	return name[0].upper()+name[1:].lower()

print()
print(list(map(normalize,["adam", "LISA", "baRT"])))

# practice 2
def prod(L):
	return reduce(lambda x, y: x * y, L)

print()
print("3 * 5 * 7 * 9 =", prod([3, 5, 7, 9]))

# practice 3
def charToNum(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def strToFloat(s):
	sFront, sBack = s.split('.')
	return reduce(lambda x, y: 10 * x + y, map(charToNum, sFront)) + reduce(lambda x, y: 0.1 * x + y, map(charToNum, sBack[-1::-1]))

print("strToFloat(\'123.456\') = ", strToFloat('123.456'))