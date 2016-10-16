print("type(123) =", type(123))
print("type(\'123\') =", type('123'))
print("type(None) = ", type(None))
print("type(abs) =", type(abs))

import types

print("type(\'abc\') == str?", type("abc") == str)

class MyObject(object):

	def __init__(self):
		self.x = 9

	def power(self):
		return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))

setattr(obj, 'y', 19)

print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

print(getattr(obj, 'z', 404))

f = getattr(obj, "power")
print(f)
print(f())