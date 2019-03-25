def bucketSort(arr, bucketSize):
	if len(arr) == 0: return arr
	minValue = min(arr)
	maxValue = max(arr)
	bucketsCount = (maxValue - minValue) // bucketSize + 1
	buckets = [[]] * bucketsCount

	for i in range(len(arr)):
		ind = (arr[i] - minValue) // bucketSize
		buckets[ind] = buckets[ind] + [arr[i]]

	arr = []
	for i in range(len(buckets)):
		buckets[i] = insertSort(buckets[i])
		for j in range(len(buckets[i])):
			arr.append(buckets[i][j])
	return arr
	
def insertSort(bucket):
	for i in range(1, len(bucket)):
		temp = bucket[i]
		j = i - 1
		while j >= 0 and bucket[j] > temp:
			bucket[j + 1] = bucket[j]
			j -= 1
		bucket[j + 1] = temp
	return bucket

arr = [78,17,39,26,72,94,21,12,23,68]
print(bucketSort(arr, 5))

# Note:
# a = [[0]] * 3
# a[1] = a[1] + [1]
# a = [[0], [0, 1], [0]]

# b = [[0]] * 3
# b[1].append(1)
# b = [[0, 1], [0, 1], [0, 1]]
