#-*- coding:utf-8 -*-
# @author: qianli
# @file: isHappy.py
# @time: 2019/08/19
# class Solution:
def isPalindrome(x):
    res = []
    x1 = x
    while x >= 10:
        b = x % 10
        x = x // 10
        res.append(b)
    res.append(x)
    return res

def sum_10(res):
    data = 0
    for i in range(len(res)):
        data += res[i] ** 2
    return data
def isHappy(n):
    data = n
    ress = []
    ress.append(data)
    while data in ress:
        data = sum_10(isPalindrome(data))
        if data == 1:
            return True
        if data in ress:
            return False
        else:
            ress.append(data)
    # clf = Solution()
print(isHappy(19))
