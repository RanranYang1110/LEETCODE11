#-*- coding:utf-8 -*-
# @author: qianli
# @file: thirdMax.py
# @time: 2019/09/17
def thirdMax(nums):
    nums = list(set(nums))
    min1, min2, min3 = float('-inf'), float('-inf'), float('-inf')
    for i in range(len(nums)):
        if nums[i] > min1:
            min1, min2, min3 = nums[i], min1, min2
        elif nums[i] > min2:
            min2, min3 = nums[i], min2
        elif nums[i] > min3:
            min3 = nums[i]
    return min1 if min3 == float("-inf") else min3
nums = [2, 3,2,1]
print(thirdMax(nums))