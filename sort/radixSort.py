import math
def LSDRadixSort(arr):
	Max = max(arr)
	radix = 0
	while(Max != 0):
		Max /= 10
		radix += 1

	for i in range(1, radix + 1):
		bukcet = [[] for i in range(10)]
		mod = pow(10, i)
		for j in range(len(arr)):
			base = arr[j] % mod
			base = base // pow(10, i - 1)
			bukcet[base].append(arr[j])
		arr = []
		for k in range(10):
			for ele in bukcet[k]:
				arr.append(ele)
	return arr

arr = [73, 22, 93, 43, 55, 14, 28, 65, 39, 81]
print(LSDRadixSort(arr))

def MSDRadixSort(arr,radix):
	n = len(arr)
	Max = max(arr)
	k = pow(10, radix - 1)
	bucket = [[] for i in range(10)]
	num = [0 for i in range(10)]

	for a in arr:
		index = (a // k) % 10
		bucket[index].append(a)
		num[index] += 1

	cnt = 0
	arr = []
	for i in range(10):
		if num[i] == 1:
			arr.append(bucket[i][0])

		elif num[i] > 1:
			B = bucket[i][:]
			B = MSDRadixSort(B, radix - 1)
			arr.extend(B)
			cnt += len(B)
	return arr

arr = [1002, 23, 897, 25, 265, 256, 24]
print(MSDRadixSort(arr, 4))