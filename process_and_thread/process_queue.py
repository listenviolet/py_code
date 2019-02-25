from multiprocessing import Process, Queue
import os, time, random

def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)
		time.sleep(random.random())

if __name__ == '__main__':
	q = Queue()
	pw = Process(target = write, args = (q, ))
	pr = Process(target = read, args = (q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()

# Process to write: 9478
# Put A to queue...
# Process to read: 9479
# Get A from queue.
# Put B to queue...
# Put C to queue...
# Get B from queue.
