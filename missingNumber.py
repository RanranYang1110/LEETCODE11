#-*- coding:utf-8 -*-
# @author: qianli
# @file: missingNumber.py
# @time: 2019/08/20
def missingNumber(nums):
    N = len(nums)
    Sum = (N+1) * N / 2
    return int(Sum - sum(nums))

a = [0,3,2]
print(missingNumber(a))