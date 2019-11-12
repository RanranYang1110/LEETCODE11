#-*- coding:utf-8 -*-
# @author: qianli
# @file: moveZeroes.py
# @time: 2019/08/09
def moveZeros(nums):
    N = len(nums)
    m = 0
    for i in range(N):
        if nums[m] == 0:
            nums.append(0)
            nums.pop(m)
            i = 0
        else:
            m += 1
    return nums

def moveZeros2(nums):
    m = 0
    for i in range(len(nums)):
        if nums[m] == 0:
            nums.pop(m)
            nums.append(0)
        else:
            m += 1
    return nums
# nums = [0,0,1]
nums = [ 0, 0, 1, 0, 3, 12, 7, 0, 3, 29, 9, 0, 1]
print(moveZeros2(nums))