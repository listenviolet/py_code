# 十大经典排序算法总结（Python）

------
参考链接：
[十大经典排序算法（动图演示)](http://www.cnblogs.com/onepixel/articles/7674659.html)
[基数排序](https://baike.baidu.com/item/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F/7875498?fr=aladdin)
[基数排序--MSD(桶排序)](https://blog.csdn.net/Anoy_acer/article/details/81047430)

[TOC]
## 0. 算法概述
### 0.1 算法分类
十种常见排序算法可以分为两大类：
> * **非线性时间比较类排序：**通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此称为非线性时间比较类排序。
> * **线性时间非比较类排序：**不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此称为线性时间非比较类排序。 

排序算法
1.非线性时间比较类排序
:    1.1 交换排序： 冒泡排序；快速排序
:    1.2 插入排序： 简单插入排序；希尔排序
:    1.3 选择排序： 简单选择排序；堆排序
:    1.4 归并排序： 二路归并排序；多路归并排序

2.线性时间非比较类排序
:    2.1 基数排序；
:    2.2 桶排序；
:   2.3 计数排序
### 0.2 时间复杂度
![time_complexity][2]
### 0.3 相关概念
> * **稳定：** 如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
> * **不稳定：** 如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
> * **时间复杂度：** 对排序数据的总的操作次数。反映当n变化时，操作次数呈现什么规律。
> * **空间复杂度：** 是指算法在计算机内执行时所需存储空间的度量，它也是数据规模n的函数。 

## 1. 冒泡排序 (Bubble Sort)
### 1.1 算法描述（升序）
1. 从前向后遍历未排序序列，如果当前元素 > 后一个元素，则交换这两个元素
2. 重复1，直到排序完成
3. **注意：**第i轮遍历后，数组的第i大的元素已移动到数组[-i]位，数组的倒数第i位至最后一位是已经排序好的最大的i个元素；那么下一轮遍历时，仅需遍历arr[:-i]中的元素即可。
### 2.2 例子
**arr:**
: [4 3 2 1]

**第1轮遍历**       
: [**3 4** 2 1]
: [3 **2 4** 1]
: [3 2 **1 *4***]

**第2轮遍历**
: [**2 3** 1 *4*]
: [2 **1 *3*** *4*]

**第3轮遍历**
: [**1 2** *3* *4*]

(其中**粗体**表示当前比较的两个元素，*斜体*表示已经排序好的元素)
### 1.3 代码实现
```python
def bubbleSort(arr):
	length = len(arr)
	for i in range(length - 1):
		for j in range(0, length - i - 1): 	
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr
```
### 1.4 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>$O(n^2)$</th>
        <th>$O(n^2)$</th>
        <th>$O(n)$</th>
        <th>$O(1)$</th>
        <th>稳定</th>
    </tr>
</table>

## 2. 选择排序 (Selection Sort)
* 每次在无序区中选择最小的元素，与无序区的第一个元素交换位置，则有序区扩展一；以此类推，直至所有元素排序完毕。

### 2.1 算法描述
1. 有序区arr[:sorted]; 无序区arr[sorted:] (sorted为已排序部分最大index;初始为0)
2. 在无序区中找到最小的元素，swap(arr[sorted], arr[minIndex])
3. sorted += 1
4. 重复1-3，直至所有元素排序完毕。

### 2.2 例子
**arr:** 
: [4 3 2 1]

**第1轮遍历**
: [**4** 3 2 **1**]
: [*1* 3 2 4]

**第2轮遍历**
: [*1* **3 2** 4]
: [*1 2* 3 4]

### 2.3 代码实现
```python
def selectionSort(arr):
	length = len(arr)
	for i in range(length - 1): # the first ind of the unsorted
		minIdx = i              # the minIdx of the unsorted
		for j in range(i+1, length):
			if arr[j] < arr[minIdx]:
				minIdx = j
		arr[i], arr[minIdx] = arr[minIdx], arr[i]
	return arr
```
### 2.4 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>$O(n^2)$</th>
        <th>$O(n^2)$</th>
        <th>$O(n)$</th>
        <th>$O(1)$</th>
        <th>不稳定</th>
    </tr>
</table>

## 3. 插入排序 (Insertion Sort)
* 对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

### 3.1 算法描述
1. 有序区 arr[:sorted]; 无序区 arr[sorted:] (初始状态认为第0个元素为已排序的，sorted = 1)
2. 取出无序区的第一个元素的值，temp = arr[sorted]
3. 将该值从后向前依次与有序区元素arr[i]比较，若temp < arr[i]，则将arr[i]后移；否则，将temp的值插入在(i+1)位置处。
4. 重复1-3直至整个数组排序完成。

### 3.2 例子
**arr**
: [1 3 2 5 4]

**第1轮**
: [*1* **3** 2 5 4] **temp = 3**
* 1为有序区第一个元素，3为无序区第一个元素。拿着数值3，从后向前遍历有序区。
* 因为3 > 1, 则将其放在有序区的后一位，即保持3的位置不变。
* 第1轮后，有序区为[1,3],无序区为[2 5 4])

**第2轮**
: [*1 3* **2** 5 4]  **temp = 2**
* 2为无序区第一个元素，拿着数值2，从后向前遍历有序区
: [*1 **3* _** 5 4]  **temp = 2**
* 首先比较 3 > temp, 则将3后移一位，继续向前遍历有序区
: [***1** _ 3* 5 4]      **temp = 2**
* 比较 1 < temp, 则将temp插入在1的后一位
: [*1 **2** 3* 5 4]
* 第2轮后，有序区为[1 2 3], 无序区为[5 4]

**第3轮**
: [*1 2 3* **5** 4] **temp = 5**
* 5为无序区第一个元素, 拿着数值5,，从后向前遍历有序区
* 因为3 < temp，则将temp插入在3的后一位，即保持5的位置不变
* 第3轮后，有序区变为[1 2 3 5],无序区为[4]

**第4轮**
: [*1 2 3 5* **4**] **temp = 4**
* 4为无序区第一个元素，拿着数值4，从后向前遍历有序区
* 因为 5 > temp, 将5后移一位，继续向前遍历有序区
: [*1 2 **3** _ 5*] **temp = 4**
* 因为3 < temp，则将temp插入在3的后一位。
: [*1 2 3 4 5*] 
* 排序完成

### 3.3 代码实现
```python
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
```
### 3.4 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>$O(n^2)$</th>
        <th>$O(n^2)$</th>
        <th>$O(n)$</th>
        <th>$O(1)$</th>
        <th>稳定</th>
    </tr>
</table>

## 4. 希尔排序 (Shell Sort)
* 希尔排序(Shell's Sort)是插入排序的一种又称“缩小增量排序”（Diminishing Increment Sort），是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法。该方法因D.L.Shell于1959年提出而得名，是第一个突破O(n2)的排序算法。
* 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
* 参考链接：[理解希尔排序的过程](https://blog.csdn.net/weixin_37818081/article/details/79202115)

### 4.1 算法描述
1. 设待排序元素序列有n个元素，首先取一个整数increment（小于n）作为间隔，将全部元素分为increment个子序列，所有距离为increment的元素放在同一个子序列中
2. 在每一个子序列中分别实行直接插入排序。
3. 然后缩小间隔increment，重复上述子序列划分和排序工作。
4. 直到最后取increment=1，将所有元素放在同一个子序列中排序为止。

### 4.2 例子
**arr** 
: [21 25 49 25* 16 8] **初始增量：** len(arr) // 3 + 1 = 3

**增量为3**
: 子序列1: [21 _ _ 25* _ _ ] => (21 < 25 直接插入排序无需交换)
: 子序列2: [ _ 25 _ _ 16 _ ] => (25 > 16 插入排序后交换) => [ _ 16 _ _ 25 _]
: 子序列3: [ _ _ 49 _ _ 8 ]  => (49 > 8 插入排序后交换)  => [ _ _ 8 _ _ 49 ]
: 合成序列: [21 16 8 25* 25 49]

**增量为2**
: 子序列1: [21 _ 8 _ 25] => (插入排序) => [8 _ 21 _ 25]
: 子序列2: [_ 16 _ 25* _ 49]
: 合成序列: [8 16 21 25* 25 49]

**增量为1**
: 当增量为1的时候，实际上就是把整个数列作为一个子序列进行插入排序
: 子序列: [8 16 21 25* 25 49]
: 合成序列: [8 16 21 25* 25 49]
: 排序完成

### 4.3 代码实现
```python
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
```

### 4.4 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>与增量选取有关</th>
        <th>$O(n^2)$</th>
        <th>$O(n)$</th>
        <th>$O(1)$</th>
        <th>不稳定</th>
    </tr>
</table>
* **增量的选择：** 希尔排序的时间复杂度与增量序列的选取有关，例如希尔增量时间复杂度为$O(n^2)$，而Hibbard增量的希尔排序的时间复杂度为$O(n^{\frac{3}{2}})$，希尔排序时间复杂度的下界是$O(nlog_2n)$。只对特定的待排序记录序列，可以准确地估算关键词的比较次数和对象移动次数。想要弄清关键词比较次数和记录移动次数与增量选择之间的关系，并给出完整的数学分析，今仍然是数学难题。
* **与快速排序对比：** 
1. 希尔排序没有快速排序算法快 (快排的平均时间复杂度为：$O(nlog_2n$))，因此中等大小规模表现良好，对规模非常大的数据排序不是最优选择； 
2. 但是希尔算法在最坏的情况下和平均情况下执行效率相差不是很多，与此同时快速排序在最坏的情况下执行的效率会非常差。

## 5. 归并排序
* 该算法是采用**分治法 (Divide and Conquer)** 的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。 

### 5.1 算法描述
1. 把长度为n的输入序列分成两个长度为n/2的子序列；
2. 对这两个子序列分别采用归并排序；
3. 将两个排序好的子序列合并成一个最终的排序序列。

### 5.2 例子
**arr** 
: [1 4 2 4 3 5]

1. left [1 4 2] 
: **divide** [1] [4 2]
: **divide** [1] / [4] [3]
: **merge** [1] / [2 4]
: **merge** [1 2 4] 

2. right[4 3 5]
: **divide** [4] / [3 5]
: **divide** [4] / [3] [5]
: **merge** [4] / [3 5]
: **merge** [3 4 5]

**merge**
: [1 2 3 4 5 6]
* merge时，分别从前向后遍历left和right，比较left[i],right[j]的大小，将较小值插入到merge后的数组中。
* 当left(或right)遍历结束后，将right(或left)的剩余元素添加到merge后的数组中。

### 5.3 代码实现
```python
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
```

### 5.4 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>$O(nlog_2n)$</th>
        <th>$O(nlog_2n)$</th>
        <th>$O(nlog_2n)$</th>
        <th>$O(n)$</th>
        <th>稳定</th>
    </tr>
</table>

## 6. 快速排序（Quick Sort）
* 快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。快速排序同样采用了**分治**的思想。

### 6.1 算法描述
1. 从数列中挑出一个元素，称为**“基准”(pivot)**；
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为**分区(partition)**操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

### 6.2 例子
取数组第0个元素的值作为pivot
初始化两个位置标记left = 0; right = len(arr) - 1
1. 比较pivot和arr[right]的大小，若pivot <= arr[right]，则right递减1；
2. 直到 pivot > arr[right] 且 left < right: 将 arr[right] 的值赋给 arr[left]。right 向前移动结束，至第 4 步，left 向后移动。
3. 若 left == right，则将pivot的值赋给arr[left]，本轮排序结束。此时，pivot之前的元素均小于pivot; pivot之后的元素均大于pivot。递归地用快速排序算法对上一轮pivot前后的两个子序列分别排序。
4. 比较pivot和arr[left]的大小，若pivot >= arr[left]，则left递增1；
5. 直到 pivot > arr[left] 且 left < right: 将 arr[left] 的值赋给 arr[right]。left 向前移动结束，至第 1 步，right 向前移动。
6. 若 left == right，转至第 3 步。

**arr:** [**3** 1 2 6 4 5] **pivot = 3**
<-- right
1. [3 1 2 6 4 5] pivot = 3; left = 0; right = 5
2. [3 1 2 6 4 5] pivot = 3; left = 0; right = 2
3. [**2** 1 **2** 6 4 5] pivot = 3; left = 0; right = 2; arr[left] = arr[right]

left-->
4. [2 1 2 6 4 5] pivot = 3; left = 2; right = 2;
5. [2 1 **3** 6 4 5] pivot = 3; left = 2; right = 2; arr[left] = pivot

对pivot前后的两个子序列递归快排：[2 1], [6 4 5],略。

### 6.3 代码实现
```python
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
```

### 6.4 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>$O(nlog_2n)$</th>
        <th>$O(n^2)$</th>
        <th>$O(nlog_2n)$</th>
        <th>$O(nlog_2n)$</th>
        <th>稳定</th>
    </tr>
</table>

* 最坏的情况在 1. 数组已经正序； 2.数组倒序； 3. 所有元素都相同 时出现。
* 这些情况下，每次分出来的子序列长度都是原序列长度 - 1 (即不包含上一轮pivot)。

## 7. 堆排序
* 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

### 7.1 数组与二叉树
> * 堆是一个近似完全二叉树的结构，并同时满足堆积的性质：
> * 大顶堆满足：子结点的键值或索引总是小于它的父节点；
> * 小顶堆满足：子结点的键值或索引总是大于它的父节点。

* **数组索引与二叉树中节点的关系：**
* 当前node的值在数组中的索引为 $i$
* 其左孩子节点对应数组索引为 $2 * i + 1$
* 其右孩子节点对应数组索引为 $2 * i + 2$
* 其父节点对应数组索引为 $(i - 1) / 2$
: 　　　4
: 　　/ 　　\
:  　 5　　　 3
: 　/　\ 　　/
: 2　　6   　1

### 7.2 堆的创建（初始化）
给定一棵二叉树，将其调整为堆有自上而下调整方式，以使其满足最大堆/最小堆的性质。
#### 7.2.1 算法描述(例子：调整为小顶堆)
1. 所有的叶子节点均可以看作已经调整为最小堆的结构；故从第一个有孩子节点的节点开始向前遍历调整，直到遍历调整根结点后停止；
2. 若当前节点node(i)的值不大于其左右孩子节点的值，则继续遍历前一个节点(即节点序号 i - 1)；
3. 若当前节点node(i)的值大于其孩子节点的值，则选择值最小的孩子节点与该节点交换，直至调整到以node(i)为根结点的子树满足最小堆的性质；继续遍历前一个节点node(i-1)。

#### 7.2.2 例子
 　　　98
 　　/ 　　\
  　 86　　　 **68**
 　/　\ 　　/
 58　　42  **42***

* 1.第一个非叶子节点为68，68 > 42*，故交换
 　　　98
 　　/ 　　\
  　 **86**　　　 42*
 　/　\ 　　/
 58　　**42**  68

* 2.继续向前遍历，到节点86；86 > 58 > 42; 将86与最小的孩子节点42交换
 　　　**98**
 　　/ 　　\
  　 **42**　　　 42*
 　/　\ 　　/
 58　　86  68

* 3.继续向前遍历，到根结点98；98 > 42 = 42*; 将98与42交换；
 　　　42
 　　/ 　　\
  　 **98**　　　 42*
 　/　\ 　　/
 **58**　　86  68

* 4.将以98为根结点的子树调整为最小堆; 98 > 86 > 58; 将98与58交换;调整完毕。
 　　　42
 　　/ 　　\
  　 58　　　42*
 　/　\ 　　/
 98　　86  68

#### 7.2.3 代码实现
**自上而下调整子树为最小堆:**(见算法描述3)
```python
# Adjust from top to bottom
# a: the arr
# i: adjust from node i
# n: the total number of nodes in heap
# j: the child of i
def MinHeapFixdown(a, i, n):

	temp = a[i]
	j = 2 * i + 1
	while j < n:
		if j + 1 < n and a[j + 1] < a[j]: # find the min of left and right child
			j += 1

		if a[j] < temp:
			a[i] = a[j]
			i = j
			j = 2 * i + 1
		else: break
	a[i] = temp
```
**最小堆的创建**（初始化）
```python
# Create the Min Heap
# Adjust from the first node which is not leaf
# Make root(i) whose heap to be the min heap
# then make the root(i - 1) whose heap to be the min heap...
def createMinHeap(a, n):
	for i in range(n // 2 - 1, -1, -1):
		MinHeapFixdown(a, i, n)
	return a
```
### 7.3 堆中元素的删除 与 堆排序
* 在堆排序中，根结点的值为当前堆的最小值，如果以此取出根结点的值，并将剩余元素重新调整为最小堆，即可将原数组元素由小到大依次取出。
* 这里就涉及到如何取出根节点的值，并调整剩余元素为最小堆的算法实现。
#### 7.3.1 算法描述
1. 取出最小堆的根的值；将当前最小堆的根的值与最后一个元素交换；
2. 利用7.1.2中"自上而下调整子树为最小堆"的方法，将前n - 1 个元素构成的树重新调整为最小堆结构。

#### 7.3.2 例子
 　　　**42**
 　　/ 　　\
  　 58　　　42*
 　/　\ 　　/
 98　　86  68
1. 取出根结点的值，加入到已排序的数组arr中，并交换42与最后一个节点68的值。
 　　　**68**
 　　/ 　　\
  　 58　　　42*
 　/　\ 　　/
 98　　86  ***42***
arr = [42]
2. 此时认为42已被删除（被删除元素用斜体标注）；对剩余的前5个元素进行调整，自上而下的调整为最小堆；
 　　　**42***
 　　/ 　　\
  　 58　　　**68**
 　/　\ 　　/
 98　　86  *42*
arr = [42]
3. 最小堆调整完毕；取出根结点的值42*，加入到已排序的数组arr中，并交换42*与最后一个节点86的值。（注意：42已被删除，最后一个节点为86.）
 　　　**86**
 　　/ 　　\
  　 58　　　68
 　/　\ 　　/
 98　　***42***  *42*
arr = [42, 42*]
4. 此时认为42*已被删除；对剩余的前4个元素进行调整，自上而下的调整为最小堆；
 　　　**58**
 　　/ 　　\
  　**86**　　 68
 　/　\ 　　/
 98　*42**  *42*
5. 最小堆调整完毕；取出根结点的值58，加入到已排序的数组arr中，并交换58与最后一个节点98的值。
 　　　**98**
 　　/ 　　\
  　86　　 68
 　/　\ 　　/
 ***58***　*42**  *42*
arr = [42, 42*, 58]
6. 同理进行调整，直至取出堆中最后一个元素，堆排序完成。arr = [42, 42*, 58, 68, 86, 98]

#### 7.3.3 代码实现
**删除当前根结点，并调整剩余元素重新构成最小堆**
```python
# Delete from the heap
def MinHeapDeleteNumber(a, n):
	a[0], a[n - 1] = a[n - 1], a[0]
	MinHeapFixdown(a, 0, n - 1)
```
**堆排序**
```python
def MinHeapSortToDescendArray(a, n):
	for i in range(n - 1, 0, -1):
		a[0], a[i] = a[i], a[0]
		MinHeapFixdown(a, 0, i)
	return a
```
#### 7.3.4 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>$O(nlog_2n)$</th>
        <th>$O(nlog_2n)$</th>
        <th>$O(nlog_2n)$</th>
        <th>$O(1)$</th>
        <th>不稳定</th>
    </tr>
</table>
### 7.4 堆中添加元素
#### 7.4.1 算法描述
1. 在一个最小堆中添加新元素，将该元素添加为该树的最后的一个节点。
2. 比较新节点的值与其父节点的值大小；若该节点的值大于父节点的值，则该子结构满足最小堆性质，可以停止调整；若该节点的值小于父节点的值，则交换该结点与其父节点，直到子结构满足最小堆性质。

#### 7.4.2 例子
 　　　42
 　　/ 　　\
  　 58　　　**42***
 　/　\ 　　/　　＼
 98　　86  68　　**36**

1.添加新元素36到已创建的最小堆中。
2.比较新节点的值36与其父节点的值; 36 < 42 不满足最小堆的性质了，需要进行调整; 交换36和其父节点42*。
 　　　**42**
 　　/ 　　\
  　 58　　　 **36**
 　/　\ 　　/　　＼
 98　　86  68　　42*
3. 比较36与其父节点的值的大小; 36 < 42; 不满足最小堆的性质，需要进行调整; 交换36和其父节点42; 调整完毕。
 　　　**36**
 　　/ 　　\
  　 58　　　 **42**
 　/　\ 　　/　　＼
 98　　86  68　　42*

#### 7.4.3 代码实现
**自下而上调整为最小堆**
```python
# Adjust from bottom to top
# a: the arr
# i: adjust from node i
# j: the parent of i
def MinHeapFixup(a, i):
	temp = a[i]
	j = (i - 1) // 2          # adjust from the first node which is not leaf
	while j >= 0 and i != 0:  # if the parent > current: current <= parent
		if a[j] > temp:   
			a[i] = a[j]
			i = j
			j = (i - 1) // 2
		else: break
	a[i] = temp
```
**向堆中添加元素**
```python
# Add a number to the heap
# a: the arr
# n: the total number of the heap
def MinHeapAddNumber(a, n, number):
	a[n] = number
	MinHeapFixup(a, n)
```

## 8. 计数排序(Counting Sort)
* 计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

### 8.1 算法描述
1. 找出待排序的数组中最大和最小的元素；
2. 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
3. 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
4. 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

### 8.2 例子
arr = [2, 3, 2, 5, 3, 1]
min = 1
max = 5
C[1]: 1
C[2]: 2
C[3]: 2
C[4]: 0 
C[5]: 1
C数组的下标即为arr数组中元素的值，arr数组中元素出现的次数，即为对应下标下C数组的值。比如arr中3出现了2次，C[3] = 2.
那么将C数组的下标按计数大小依次读出，即可获得arr中元素的值从小到大的排列。
得到：arr = [1, 2, 2, 3, 3, 5]

### 8.3 代码实现
```python
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
```
### 8.4 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>$O(n+k)$</th>
        <th>$O(n+k)$</th>
        <th>$O(n+k)$</th>
        <th>$O(n+k)$</th>
        <th>稳定</th>
    </tr>
</table>

## 9.桶排序(Bucket Sort)
* 桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。
### 9.1 算法描述
1. 根据所给数据的大小范围，划定合理的所分的桶数，则第i桶中所盛放的数据的大小范围为：[i * bucketsize, (i + 1) * bucketsize]
2. 遍历输入数组，并把数据一个个放到所对应的桶中
3. 对每个不是空的桶进行排序(本例子中用的插入排序)
4. 从不是空的桶中把排好序的数据拼接起来
### 9.2 例子
设有数组 array = [63, 157, 189, 51, 101, 47, 141, 121, 157, 156, 194, 117, 98, 139, 67, 133, 181, 13, 28, 109]，对其进行桶排序
1. 设定分5个桶，每个桶的大小为36.4
2. 那么所分的桶的区间分别为：[13,49.4), [49.4, 85.8), [85.8, 122.2), [122.2, 158.6), [158.6, 195)
3. 遍历输入数据，将数据一个个放入对应的桶中。之后对每个桶中的数据进行插入排序。
index = 0
[13,49.4) => 13 -> 28 -> 47

index = 1
[49.4, 85.8)=> 51 -> 63 -> 67

index = 2
[85.8, 122.2) => 98 -> 101 -> 109 -> 117 -> 121

index = 3
[122.2, 158.6) => 133 -> 139 -> 141 -> 156 -> 157 -> 157

[158.6, 195) => 181 -> 189 -> 194
4. 合并数据。bucket 0 -> bucket 1 -> bucket 2 -> bucket3 -> bucket 4
5. 最终数据。 [13, 28, 47, 51, 63, 67, 98, 101, 109, 117, 121, 133, 139, 141, 156, 157, 157]
### 9.3 代码实现
```python
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
```
### 9.4 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>$O(n+k)$</th>
        <th>$O(n^2)$</th>
        <th>$O(n)$</th>
        <th>$O(n+k)$</th>
        <th>稳定</th>
    </tr>
</table>
## 10.基数排序(Radix Sort)
**LSD 最低位优先(Least Significant Digit first)法** 
基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。
**MSD 最高位优先(Most Significant Digit first)法**
先按k1排序分组，同一组中记录，关键码k1相等，再对各组按k2排序分成子组，之后，对后面的关键码继续这样的排序分组，直到按最次位关键码kd对各子组排序后。再将各组连接起来，便得到一个有序序列。

### 10.1 算法描述
#### 10.1.1 LSD算法描述
1. 取得数组中的最大数，并取得位数；
2. 以个位元素为索引，对数组元素进行计数排序
3. 合并数组；
4. 之后，依次以十位，...，最大元素的最大位数处的值为索引，进行计数排序，并合并数组；
5. 最后可得完全排序后的数组。
#### 10.1.2 MSD算法描述
1. 先根据最高位关键码K1排序，得到若干对象组，对象组中每个对象都有相同关键码K1。
2. 再分别对每组中对象根据关键码K2进行排序，按K2值的不同，再分成若干个更小的子组，每个子组中的对象具有相同的K1和K2值。
3. 依此重复，直到对关键码Kd完成排序为止。
4. 最后，把所有子组中的对象依次连接起来，就得到一个有序的对象序列。

### 10.2 例子
#### 10.2.1 LSD举例
arr = [73, 22, 93, 43, 55, 14, 28, 65, 39, 81]
1. 首先根据个位数的数值，在走访数值时将它们分配至编号0到9的桶子中：
0:
1: 81
2: 22
3: 73 93 43
4: 14
5: 55 65
6:
7:
8: 28
9: 39
2. 接下来将这些桶子中的数值重新串接起来，成为数列：arr = [81, 22, 73, 93, 43, 14, 55, 65, 28, 39]
3. 根据十位数来分配：
0:
1: 14
2: 22 28
3: 39
4: 43
5: 55
6: 65
7: 73
8: 81
9: 93
4. 接下来将这些桶子中的数值重新串接起来，成为数列：arr = [14, 22, 28, 39, 43, 55, 65, 73, 81, 93], 整个数列已经排序完毕。
#### 10.2.2 MSD举例
arr = [12, 14, 54, 5, 6, 3, 9, 8, 47, 89]
1. 按照最高位十位遍历并分桶：
0:   5 6 3 9 8
1:   12 14  
2:         
3:        
4:    47    
5:    54    
6:        
7:        
8:    89    
9:  
2. 然后再将每个桶分0-9号小桶
例如，对于0号桶，分小桶后：
0        
1        
2         
3:     3    
4         
5:     5    
6:     6    
7        
8:     8    
9:     9  
3. 分配结束后。接下来将所有桶中所盛数据按照桶号由小到大（桶中由顶至底）依次重新收集串起来，得到如下的数据序列：arr = [3, 5, 6, 8, 9, 12, 14, 47, 54, 89]
### 10.3 代码实现
#### 10.3.1 LSD代码
```python
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
```
#### 10.3.2 MSD代码
```python
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
```
### 10.4 LSD 算法复杂度
<table>
    <tr>
        <th>时间复杂度(平均)</th>
        <th>时间复杂度(最坏)</th>
        <th>时间复杂度(最好)</th>
        <th>空间复杂度</th>
        <th>稳定性</th>
    </tr>
    <tr>
        <th>$O(n*k)$</th>
        <th>$O(n*k)$</th>
        <th>$O(n*k)$</th>
        <th>$O(n+k)$</th>
        <th>稳定</th>
    </tr>
</table>
**LSD时间效率：** 设待排序列为n个记录，d个关键码，关键码的取值范围为radix，则进行链式基数排序的时间复杂度为O(d(n+radix))，其中，一趟分配时间复杂度为O(n)，一趟收集时间复杂度为O(radix)，共进行d趟分配和收集。 
**LSD与MSD比较：** LSD的基数排序适用于位数小的数列，如果位数多的话，使用MSD的效率会比较好。