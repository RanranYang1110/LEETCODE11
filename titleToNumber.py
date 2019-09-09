#-*- coding:utf-8 -*-
# @author: qianli
# @file: titleToNumber.py
# @time: 2019/08/20
def titleToNumber(s):
    values = []
    for i in range(65, 91):
        values.append(chr(i))
    keys = []
    for i in range(1,27):
        keys.append(i)
    dict_a = dict(zip(values, keys))
    mm = 0
    N = len(s)
    for i in range(N):
        mm += 26 ** (N - i -1) * dict_a[s[i]]
    return mm
print(titleToNumber('AAA'))