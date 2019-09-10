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

nums = [2,4,3,11,8,6,9,4]
print(bubbleSort(nums))