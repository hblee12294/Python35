import time, threading

def loop():
	print("thread %s is running..." % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print("thread %s >>> %s" % (threading.current_thread().name, n))
		time.sleep(1)
	print("thread %s ended." % threading.current_thread().name)  

print("Threading %s is running..." % threading.current_thread().name)          # MainThread 
t= threading.Thread(target = loop, name = "LoopThread")         # create a new thread called "LoopThread"
t.start()
t.join()
print("Tread %s ended." % threading.current_thread().name)