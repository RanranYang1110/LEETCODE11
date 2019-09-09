#-*- coding:utf-8 -*-
# @author: qianli
# @file: isPowerOfTwo.py
# @time: 2019/09/06
def isPowerOfTwo(n):
    '''给定一个整数，编写一个函数来判断它是否是2的幂次方'''
    if n < 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return isPowerOfTwo(n // 2)
print(isPowerOfTwo(2))
