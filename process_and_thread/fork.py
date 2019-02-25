import os 
print('Process (%s) start...' % os.getpid())
# os.getoid(): return the main process pid
pid = os.fork()
print("pid:",pid)
# os.fork() create a child process and returns 2 times.
# for parent process: os.fork() return child process pid
# for child process: os.fork() return 0

if pid == 0:
	print("Child process returns 0.")
	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
	print("Main process returns the child process pid: ", pid)
	print('I (%s) just created a child prcess (%s).' % (os.getpid(), pid))