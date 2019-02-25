import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server %s' % server_addr)

m = QueueManager(address = (server_addr, 5000), authkey = b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
	try:
		n = task.get(timeout = 1)
		print('run task %d * %d...' % (n, n))
		r = '%d * %d = %d' % (n, n, n * n)
		time.sleep(1)
		result.put(r)
	except queue.Empty:
		print('task queue empty.')

print('worker exit')

# $ python task_master.py 
# Put task 9261...
# Put task 9624...
# Put task 9518...
# Put task 5942...
# Put task 2607...
# Put task 6020...
# Put task 8244...
# Put task 3177...
# Put task 3295...
# Put task 1556...
# Try get result
# Result: %s 9261 * 9261 = 85766121
# Result: %s 9624 * 9624 = 92621376
# Result: %s 9518 * 9518 = 90592324
# Result: %s 5942 * 5942 = 35307364
# Result: %s 2607 * 2607 = 6796449
# Result: %s 6020 * 6020 = 36240400
# Result: %s 8244 * 8244 = 67963536
# Result: %s 3177 * 3177 = 10093329
# Result: %s 3295 * 3295 = 10857025
# Result: %s 1556 * 1556 = 2421136
# master exit.

# $ python task_worker.py 
# Connect to server 127.0.0.1
# run task 9261 * 9261...
# run task 9624 * 9624...
# run task 9518 * 9518...
# run task 5942 * 5942...
# run task 2607 * 2607...
# run task 6020 * 6020...
# run task 8244 * 8244...
# run task 3177 * 3177...
# run task 3295 * 3295...
# run task 1556 * 1556...
# worker exit
