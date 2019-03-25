def shellSort(start, end, number):
	increment = end - start + 1
	while increment > 1:
		increment //= 3 + 1

		for i in range(start + increment, end + 1):
			if (number[i - increment] > number[i]):
				temp = number[i]
				j = i - increment
				while (j >= start and number[j] > temp):
					number[j + increment] = number[j]
					j -= increment
				number[j + increment] = temp
	return number


number = [1,3,2,5,4,6]
print(shellSort(0, len(number) - 1, number))

# https://blog.csdn.net/weixin_37818081/article/details/79202115