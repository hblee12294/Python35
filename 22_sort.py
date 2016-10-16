print(sorted([26, 5, -12, 9, -21]))
print(sorted([26, 5, -12, 9, -21], key=abs))
print(sorted(["bob", "about", "Zoo", "Credit"]))
print(sorted(["bob", "about", "Zoo", "Credit"], key=str.lower))

# practice
L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]

def byName(t):
	return t[0]

L2 = sorted(L, key=byName)
print(L2)

def byScore(t):
	return t[1]

L2 = sorted(L, key=byScore)
print(L2)