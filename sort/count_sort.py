def countSort(arr, Max):
	bucket = [0] * (Max + 1)
	for i in range(len(arr)):
		bucket[arr[i]] += 1

	idx = 0
	for i in range(len(bucket)):
		while(bucket[i] > 0):
			arr[idx] = i 
			idx += 1
			bucket[i] -= 1
	return arr

arr = [1,3,2,4,6,5]
Max = max(arr)
print(countSort(arr, Max))