import itertools

naturals = itertools.count(1)
for n in naturals:
	print(n)
	if n >= 10:
		break

cs = itertools.cycle("ABC")
t = 10
for c in cs:
	print(c)
	t = t -1
	if t == 0:
		break