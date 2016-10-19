import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
	pass

# register queues
QueueManager.register("get_task_queue", callable = lambda: task_queue)
QueueManager.register("get_result_queue", callable = lambda: result_queue)

manager = QueueManager(address = ('', 5000), authkey = b"abc")  # set port 5000, auther key = "abc"

manager.start()  # start Queue

task = manager.get_task_queue()
result = manager.get_result_queue()

# put tasks into queue
for i in range(10):
	n = random.randint(0, 10000)
	print("Put task %d..." % n)
	task.put(n)

# get result from queue
print("Try get resluts...")
for i in range(10):
	r = result.get(timeout = 10)
	print("Result: %s" % r)

manager.shutdown()
print("master exit.")