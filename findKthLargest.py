#-*- coding:utf-8 -*-
# @author: qianli
# @file: findKthLargest.py
# @time: 2019/09/16

def findKthLargest(nums, k):
    '''在未排序的数组中找到第k个最大的元素'''
    nums_sort = quicksort(nums)
    return nums_sort[k-1]
def quicksort(array):
    '''快速排序'''
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(greater) + [pivot] + quicksort(less)


nums=[3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums, k))

quicksort(nums)