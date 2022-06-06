"""
@Anthor: freya.yang
@Time: 2022/5/12 3:53 下午
@File: 0.基础排序.py
@description:
"""

"""
【冒泡排序】：
相邻的两个元素进行比较，然后把较大的元素放到后面（正向排序），在一轮比较完后最大的元素就放在了最后一个位置，
因为这一点像鱼儿在水中吐的气泡在上升的过程中不断变大，所以得名冒泡排序。
在该排序算法中，要遍历n-1轮，每一轮都要比较数组中的元素，所以时间复杂度是O(n2)
"""
def maopao(lis):
    for i in range(1, len(lis)-1):  #比较的次数
        for j in range(len(lis)-i):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis

"""
【选择排序】
第一轮的时候，所有的元素都和第一个元素进行比较，如果比第一个元素大，就和第一个元素进行交换，在这轮比较完后，就找到了最小的元素；
第二轮的时候所有的元素都和第二个元素进行比较找出第二个位置的元素，以此类推。
每遍历一次排好一个元素，而每一次都会比较所有的元素，所以时间复杂度为O(n2)。
"""
def xuanze(lis):
    for i in range(len(lis)-1):
        for j in range(i, len(lis)):
            if lis[i] > lis[j]:
                lis[i], lis[j] = lis[j], lis[i]
    return lis

"""
【快速排序】
快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort）
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

步骤为：
从数列中挑出一个元素，称为"基准"（pivot），一般是第一个元素。
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
最优时间复杂度：O(nlogn)
最坏时间复杂度：O(n2)
稳定性：不稳定

"""
def quck_sort(lis):
    if len(lis) >= 2:
        bas = lis[0]
        left, right = [], []
        for i in lis[1:]:
            if i < bas:
                left.append(i)
            else:
                right.append(i)
        return quck_sort(left) + [bas] + quck_sort(right)
    else:
        return lis

# 匿名函数写法
quick_sort = lambda lis: lis if len(lis)<=1 else quick_sort([item for item in lis[1:] if item < lis[0]]) \
                                                 +[lis[0]] + quick_sort([item for item in lis[1:] if item >= lis[0]])


"""
插入排序
插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
把n个待排序的元素看成为一个有序表和一个无序表。开始时有序表中只包含1个元素，无序表中包含有n-1个元素，排序过程中每次从无序表中取出第一个元素，将它插入到有序表中的适当位置，使之成为新的有序表，重复n-1次可完成排序过程。

1、原理
从第二个元素开始和前面的元素进行比较，如果前面的元素比当前元素大，则将前面元素 后移，当前元素依次往前，直到找到比它小或等于它的元素插入在其后面
然后选择第三个元素，重复上述操作，进行插入
依次选择到最后一个元素，插入后即完成所有排序
"""
def insert_sort(lis):
    for i in range(1, len(lis)):
        current = lis[i]
        pre_index = i -1
        while pre_index >= 0 and lis[pre_index] > current:
            lis[pre_index+1] = lis[pre_index]
            pre_index -= 1
        lis[pre_index+1] = current
    return lis

lis = [3, 1, 4, 2, 6, 5, 7, 3, 8, 1, 9]
print(xuanze(lis))