#-*- coding:utf-8 -*-
# @author: qianli
# @file: bubbleSort.py
# @time: 2019/09/10
def bubbleSort(nums):
    '''冒泡排序法'''
    N = len(nums)
    for i in range(0, len(nums)):
        for j in range(1, len(nums)-i):
            if nums[j] < nums[j-1]:
                a = nums[j-1]
                nums[j-1] = nums[j]
                nums[j] = a
    return nums

def selectionSort(nums):
    '''
    选择排序法
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    以此类推，直到所有元素均排序完毕
    '''
    aa = []
    N = len(nums)
    while len(nums) > 1:
        for j in range(1, len(nums)):
            min_value = nums[0]
            if nums[j] < min_value:
                min_value = nums[j]
        aa.append(min_value)
        nums.remove(min_value)
    aa.append(nums[0])
    return aa

def quicksort(array):
    '''快速排序'''
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def insertSort(nums):
    '''插入排序'''
    for i in range(1,len(nums)):
        data = nums[i]
        for j in range(0, i):
            if nums[j] > data:
                aa = nums[j:i]
                nums[j] = data
                nums[j+1:i+1] = aa
                break
    return nums

def shellSort(nums):
    '''希尔排序'''
    gap = 2
    while gap < len(nums) // 2:
        mm = len(nums) // gap
        for i in range(mm):
            data = nums[i::mm]
            data = insertSort(data)
            nums[i::mm] = data
        gap += 1
    nums = insertSort(nums)
    return nums

def mergeSort(nums):
    '''归并排序'''
    gap = 2
    while gap < len(nums):
        N = len(nums) // gap
        for i in range(N):
            data = nums[i::N]
            data = insertSort(data)
            nums[i::N] = data
        gap *= 2
    nums = insertSort(nums)
    return nums

nums1 = [2,4,3,11,8,6,9,4,15,19]
# nums1 = [4, 2]
# print(bubbleSort(nums1))
# print(selectionSort(nums1))
# print(insertSort(nums1))
print(shellSort(nums1))
print(mergeSort(nums1))