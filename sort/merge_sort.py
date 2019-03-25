def mergeSort(arr):
	if len(arr) < 2:
		return arr
	middle = len(arr) // 2
	left_arr = arr[:middle]
	right_arr = arr[middle:]
	return merge(mergeSort(left_arr), mergeSort(right_arr))

def merge(left_arr, right_arr):
	result = []
	i, j = 0, 0
	while i < len(left_arr) and j < len(right_arr):
		if left_arr[i] < right_arr[j]:
			result.append(left_arr[i])
			i += 1
		else:
			result.append(right_arr[j])
			j += 1
	if i == len(left_arr):
		result.extend(right_arr[j:])
	elif j == len(right_arr):
		result.extend(left_arr[i:])
	return result

arr = [1,3,2,5,4]
print(mergeSort(arr))