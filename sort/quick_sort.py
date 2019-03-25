def quickSort(arr):
	if len(arr) == 0: return []
	if len(arr) == 1: return arr
	left = 0
	right = len(arr) - 1
	base = arr[left]

	while(left < right):
		while(arr[right] > base and right > left):
			right -= 1
		if right > left:
			arr[left] = arr[right]
			left += 1
		while(arr[left] < base and left < right):
			left += 1
		if right > left:
			arr[right] = arr[left]
			right -= 1

	if left == right:
		arr[left] = base
		result = quickSort(arr[:left]) + [arr[left]]
		if left < len(arr) - 1:
			result = result + quickSort(arr[left + 1:])
		return result

arr = [1,3,2,5,4]
print(quickSort(arr))