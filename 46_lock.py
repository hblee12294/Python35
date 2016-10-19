import time, threading

balance = 0

def changeIt(n):
	global balance
	balance = balance + n
	balance = balance - n

def runThread(n):
	for i in range(100000):
		changeIt(n)

t1 = threading.Thread(target = runThread, args = (5,))
t2 = threading.Thread(target = runThread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

blance = 0 
lock = threading.Lock()

def run_thread(n):
	for i in range(100000):
		lock.acquire()         # get lock
		try:
			changeIt(n)
		finally:
			lock.release()    # cancel lock

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)