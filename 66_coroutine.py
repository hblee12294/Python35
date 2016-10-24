def consumer():
	r = ''
	while True:
		n = yield r     # valued by .send(x), then n = x, and return next r
		if not n:
			return
		print("[CONSUMER] consuming %s..." % n)
		r = "200 OK"     # that's the next r
		# r = n + 100    # give it a try

def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print("[PRODUCE] producing %s..." % n)
		r = c.send(n)                          # get r from func consumer, more specific, "yield r"
		print("[PRODUCER] Consumer return: %s" % r)
	c.close()

c = consumer()
produce(c)