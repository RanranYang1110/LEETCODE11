#-*- coding:utf-8 -*-
# @author: qianli
# @file: minMoves.py
# @time: 2019/09/17
def minMoves(nums):
    sum1 = sum(nums)
    N = len(nums)
    q = max(nums) - min(nums)
    sum2  = sum1
    while (q * N - sum1) % (N - 1) != 0 or sum2 % N !=0:
        q += 1
        sum2 = sum1 + N - 1
    return q
nums = [2,3,1]
print(minMoves(nums))