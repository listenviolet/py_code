# -----*****
#      |
# <----
#  =
# '|' the first element of unsorted arr
# search backwards the sorted arr
# insert the '|' in right place

def insertionSort(arr):
	length = len(arr)
	for i in range(1, length):  # the current element index
		preIndex = i - 1        # the index to insert
		current = arr[i]        # save the number otherwise it will be replace by others
		while(preIndex >= 0 and arr[preIndex] > current):
			arr[preIndex + 1] = arr[preIndex]  # move -->
			preIndex -= 1
		arr[preIndex + 1] = current
	return arr

arr = [5,4,3,2,1]
sorted_arr = insertionSort(arr)
print(sorted_arr)