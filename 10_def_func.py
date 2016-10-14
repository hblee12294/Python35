# -*- coding:utf-8 -*-

import math

def quadratic(a, b, c):

	if not isinstance(a, (int, float)):
		raise TypeError("%s is not a int or float" %a)
	if not isinstance(b, (int, float)):
		raise TypeError("%s is not a int or float" %b)
	if not isinstance(c, (int, float)):
		raise TypeError("%s is not a int or float" %c)

	delta = b**2 - 4*a*c

	if delta < 0:
		raise ValueError("No real roots.")
	else:
		x1 = (-b + math.sqrt(delta)) / 2*a
		x2 = (-b - math.sqrt(delta)) / 2*a
		return x1, x2

print("%0.2f, %0.2f" %quadratic(2,7,4))
print("%0.2f, %0.2f" %quadratic(1,2,1))
print(quadratic(5,3,5))