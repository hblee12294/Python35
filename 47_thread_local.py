import threading

local_school = threading.local()

def process_student():                 # process
	std = local_school.student         # get var "std" from local_school, add attribute "student"
	print("Hello, %s (in %s)" % (std, threading.current_thread().name))

def process_thread(name):
	local_school.student = name        # store argument "name" into localp
	process_student()

t1 = threading.Thread(target = process_thread, args = ('A',), name = "Thread A")
t2 = threading.Thread(target = process_thread, args = ('B',), name = 'Thread B')
t1.start()
t2.start()
t1.join()
t2.join()