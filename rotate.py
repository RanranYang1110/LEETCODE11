#-*- coding:utf-8 -*-
# @author: qianli
# @file: rotate.py
# @time: 2019/08/20
def rotate(nums, k):
    n = len(nums)
    k %= n
    for _ in range(k):
        nums.insert(0, nums.pop())
    return nums
nums = [2,5,6,8,7,5]
k = 10
nums1 = rotate(nums, k)


