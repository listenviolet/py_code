import math
def LSDBucketSort(arr):
	Max = max(arr)
	radix = 0
	while(Max != 0):
		Max = Max // 10
		radix += 1
	for i in range(1, radix + 1):
		bucket = [[]] * 10
		mod = pow(10, i)
		for j in range(len(arr)):
			base = arr[j] % mod
			base = base // pow(10, i - 1)
			bucket[base] = bucket[base] + [arr[j]]
		arr = []
		
		for k in range(10): # iterate the buckets
			for ele in bucket[k]:			
				arr.append(ele)
	return arr

arr = [192,221,12,23]
print(LSDBucketSort(arr))

