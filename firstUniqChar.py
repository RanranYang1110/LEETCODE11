#-*- coding:utf-8 -*-
# @author: qianli
# @file: firstUniqChar.py
# @time: 2019/09/04
def firstUniqChar(s):
    res = {}
    mm = {}
    for i in range(len(s)):
        if s[i] not in res:
            res[s[i]] = 1
            mm[s[i]] = i
        else:
            res[s[i]] += 1
    for key, values in list(res.items()):
        if values == 1:
            return key
s = 'mmcesd'
print(firstUniqChar(s))
ress = firstUniqChar(s)