#-*- coding:utf-8 -*-
# @author: qianli
# @file: isAnagram.py
# @time: 2019/09/05
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    ss = sorted(list(s))
    tt = sorted(list(t))
    return ss == tt

s = 'aab'
t = 'abb'
print(isAnagram(s,t))
