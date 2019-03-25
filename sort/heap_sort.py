""" Min Heap
"""

# Adjust from bottom to top
# a: the arr
# i: adjust from node i
# j: the parent of i
def MinHeapFixup(a, i):
	temp = a[i]
	j = (i - 1) // 2          # adjust from the first node which is not leaf
	while j >= 0 and i != 0:  # if the parent > current: current <= parent
		if a[j] > temp:   
			a[i] = a[j]
			i = j
			j = (i - 1) // 2
		else: break
	a[i] = temp


# Adjust from top to bottom
# a: the arr
# i: adjust from node i
# n: the total number of nodes in heap
# j: the child of i
def MinHeapFixdown(a, i, n):

	temp = a[i]
	j = 2 * i + 1
	while j < n:
		if j + 1 < n and a[j + 1] < a[j]: # find the min of left and right child
			j += 1

		if a[j] < temp:
			a[i] = a[j]
			i = j
			j = 2 * i + 1
		else: break
	a[i] = temp

# Create the Min Heap
# Adjust from the first node which is not leaf
# Make root(i) whose heap to be the min heap
# then make the root(i - 1) whose heap to be the min heap...
def createMinHeap(a, n):
	for i in range(n // 2 - 1, -1, -1):
		MinHeapFixdown(a, i, n)
	return a

def MinHeapSortToDescendArray(a, n):
	for i in range(n - 1, 0, -1):
		a[0], a[i] = a[i], a[0]
		MinHeapFixdown(a, 0, i)
	return a

a = [1,3,2,4,6,5]
a = createMinHeap(a, len(a))
a = MinHeapSortToDescendArray(a, len(a))
print(a)
# [6, 5, 4, 3, 2, 1]


# Add a number to the heap
# a: the arr
# n: the total number of the heap
def MinHeapAddNumber(a, n, number):
	a[n] = number
	MinHeapFixup(a, n)

# Delete from the heap
def MinHeapDeleteNumber(a, n):
	a[0], a[n - 1] = a[n - 1], a[0]
	MinHeapFixdown(a, 0, n - 1)