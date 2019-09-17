#-*- coding:utf-8 -*-
# @author: qianli
# @file: findContentChildren.py
# @time: 2019/09/17
def findContentChildren(g, s):
    g = sorted(g)
    s = sorted(s)
    i, j = 0, 0
    res = 0
    while i<len(g) and j<len(s):
        if g[i] <= s[j]:
            res += 1
            i += 1
            j += 1
        elif g[i] > s[j]:
            j += 1
    return res

g = [1,2,3]