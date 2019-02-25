import time, threading, random

balance1 = 0
balance2 = 0

def change_it(n):
	global balance1
	balance1 += n
	balance1 -= n

def run_thread(n):
	for i in range(1000000):
		change_it(n)

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))

t1.start()
t2.start()
t1.join()
t2.join()
print("balance1:", balance1)
# 5
# --------------------------------------
lock = threading.Lock()

def change_it_with_lock(n):
	global balance2
	balance2 += n
	balance2 -= n

def run_thread_with_lock(n):
	for i in range(1000000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

# 当某个线程开始执行change_it()时，
# 该线程因为获得了锁，
# 因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
# 由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。

t3 = threading.Thread(target = run_thread_with_lock, args = (5,))
t4 = threading.Thread(target = run_thread_with_lock, args = (8,))
t3.start()
t4.start()
t3.join()
t4.join()
print("balance2:", balance2)
