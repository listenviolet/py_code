from multiprocessing import Pool
import os, time, random 

def long_time_task(name):
	print('run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('task %s (%s) runs %0.2f seconds.' % (name, os.getpid(), (end - start)))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())

	pool = Pool(4)

	for i in range(5):
		pool.apply_async(long_time_task, args = (i, ))
	print('waiting for all subprocesses done...')
	pool.close()
	pool.join()
	print('all subprocesses done.')

# Parent process 23978.
# waiting for all subprocesses done...
# run task 0 (23979)...
# run task 1 (23980)...
# run task 2 (23981)...
# run task 3 (23982)...
# task 0 (23979) runs 0.02 seconds.
# run task 4 (23979)...
# task 3 (23982) runs 0.33 seconds.
# task 1 (23980) runs 1.06 seconds.
# task 2 (23981) runs 1.63 seconds.
# task 4 (23979) runs 2.21 seconds.
# all subprocesses done.

# Tips
# After the task0 finished, the pool not full
# then the task 4 can add to the pool.

# close() must be called before calling join()
