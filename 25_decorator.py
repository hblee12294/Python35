def log(func):
	def wrapper(*args, **kw):
		print("call %s():" % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print("2016.10.16")

now()

# ---------------
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print("%s %s():" % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log("execcute")
def now():
	print("2016-10-16")

now()

#-----
import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print("%s %s():" % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log("execcute")
def now():
	print("2016-10-16")

now()


# practice
print()

def log(func):
	def wrapper(*args, **kw):
		print("begin call")
		function = func(*args, **kw)
		print("end call")
		return function
	return wrapper

@log
def now():
	print("2016-10-16")

now()
