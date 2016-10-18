from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print("Run task %s (%s)..." % (name, os.getpid()))

	start = time.time()                   # stamp for start
	time.sleep(random.random() * 3)       # hold on for random time
	end = time.time()                     # stamp for end

	print("Task %s runs %0.2f seconds." % (name, (end - start)))  # get runtime by ( end - start)

if __name__ == "__main__":
	print("Parent process %s." % os.getpid())   # get parent process 
	p = Pool(4)                               # creat a pool for 4 processes
	for i in range(5):                               # 'i' is process name
		p.apply_async(long_time_task, args = (i,))   # creat 5 processes, the last one have to wait
	print("Waiting for all subprocess done...")
	p.close()                                      # close the pool
	p.join()                                       # wait for all processes end
	print("All subprocess done.")