#-*- coding:utf-8 -*-
# @author: qianli
# @file: isPowerOfThree.py
# @time: 2019/08/20
def isPowerOfThree(n):
    if n == 0:
        return False
    else:
        while n > 1:
            if n % 3 == 0:
                n = n / 3
            else:
                return False
        return True
print(isPowerOfThree(3))