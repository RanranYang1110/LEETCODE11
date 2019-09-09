#-*- coding:utf-8 -*-
# @author: qianli
# @file: findAnagrams.py
# @time: 2019/09/05
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    ss = sorted(list(s))
    tt = sorted(list(t))
    return ss == tt
def findAnagrams(s, p):
    aa = []
    if len(p) > len(s):
        return None
    else:
        pp = sorted(list(p))
        for i in range(0, len(s)-len(p) + 1):
            ss1 = sorted(list(s[i:i+len(p)]))
            if ss1 == pp:
                aa.append(i)
        return aa


s = 'abab'
p = 'ab'
print(findAnagrams(s, p))