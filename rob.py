#-*- coding:utf-8 -*-
# @author: qianli
# @file: rob.py
# @time: 2019/08/26
def rob(nums):
    a1 = sum(nums[::2])
    a2 = sum(nums[1::2])
    return max(a1,a2)
nums = [1,2,3,1]
nums = [2, 7, 9, 3, 1]
nums = []
print(rob(nums))