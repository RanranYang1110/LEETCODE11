#-*- coding:utf-8 -*-
# @author: qianli
# @file: findNthDigit.py
# @time: 2019/09/17
def findNthDigit(n):
    '''寻找第n个数字'''
    if n <= 9:
        return n
    mm = 1
    while n > 9 * mm * 10 ** (mm - 1):
        n -= 9 * mm * 10 ** (mm - 1)
        mm += 1

    p = n % mm
    if p == 0:
        p = mm
    q = (n - 1) // mm
    res = str(10 ** (mm - 1) + q)
    return int(res[p-1])

n = 28
print(findNthDigit(n))