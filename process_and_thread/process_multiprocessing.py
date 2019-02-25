from multiprocessing import Process
import os 

def run_proc(name, arg2):
	print('---------')
	print("Run child process %s (%s)..." % (name, os.getpid()))
	print(arg2)
	print('---------')

def child_process_2(name):
	print('========')
	print('Run child process %s (%s)...' % (name, os.getpid()))
	print('========')

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())

	p = Process(target = run_proc, args = ('test_child_1','arg2'))
	p2 = Process(target = child_process_2, args = ('test_child_2',))

	print('Child process will start.')
	p.start()
	p2.start()
	print('between start and join')
	print('between start and join')
	print('between start and join')
	print('between start and join')
	p.join()
	print('Child process 1 end.')
	print('Child process 1 end.')
	print('Child process 1 end.')
	print('Child process 1 end.')
	p2.join()
	print('Child process 2 end.')

# Sometimes: "between" < run_proc
# Sometimes: run_proc < "between"