#-*- coding:utf-8 -*-
# @author: qianli
# @file: reverseString.py
# @time: 2019/08/27
def reverseString(s):
    '''反正字符串'''
    s[0::] = s[::-1]
    return s

def reverseString2(s):
    '''反转字符串'''
    for i in range(len(s)):
        s.insert(i, s.pop())
    return s
s = ['a','b','v','d','f']
print(reverseString2(s))
