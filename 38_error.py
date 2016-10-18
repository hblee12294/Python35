
try:
	print("try...")
	r = 10 / int('5')
	print("result:", r)
except ValueError as e:
	print("ValueError:", e)
except ZeroDivisionError as e:
	print("ZeroDivisionError:", e)
else:
	print("no error!")
finally:
	print("finally...")
print("END")

# logging

import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

main()
print('End')