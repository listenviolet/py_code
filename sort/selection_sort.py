# ------*****
#       |  =
# '-' : sorted
# '*' : not sorted
# '|' : the first of the unsorted
# '=' : the min of the unsorted
# exchange('|' , '=')

# After num traverse, the min num number are sorted.

def selectionSort(arr):
	length = len(arr)
	for i in range(length - 1): # the first ind of the unsorted
		minIdx = i              # the minIdx of the unsorted
		for j in range(i+1, length):
			if arr[j] < arr[minIdx]:
				minIdx = j
		arr[i], arr[minIdx] = arr[minIdx], arr[i]
	return arr

arr = [5,4,2,6,3]
sorted_arr = selectionSort(arr)
print(sorted_arr)

