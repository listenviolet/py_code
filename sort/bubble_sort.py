# Everytime traverse the whole arr:
# 	Everytime compare the arr[i] and arr[i+1]
# 	Exchange them if arr[i] > arr[i+1]
# After i's traverse the whole arr
# The last i numbers are sorted

def bubbleSort(arr):
	length = len(arr)
	for i in range(length - 1):                    # traverse times
		for j in range(0, length - i - 1):         # loop though the whole arr	
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

arr = [1,3,5,2,4,6]
print(bubbleSort(arr))

