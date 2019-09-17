#-*- coding:utf-8 -*-
# @author: qianli
# @file: minMoves.py
# @time: 2019/09/17
def minMoves(nums):
    sum1 = sum(nums)
    N = len(nums)
    q = 0
    while (q * N - sum1) % (N - 1) != 0:
        q += 1
    return q