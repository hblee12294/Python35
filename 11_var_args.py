# -*- coding:utf-8 -*-

def hello(greeting, *args):
	if (len(args) == 0):
		print("%s!" % greeting)
	else:
		print("%s, %s!" % (greeting, args))
		print("%s, %s!" % (greeting, ', '.join(args)))

hello("Hi")
hello("Hi", "Sarah")
hello("Hello", "Michael", "Bob", "Adam")

names = ("Bart", "Lisa")
hello("Hello", *names) # turning tuple 'names' to var_args