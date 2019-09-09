#-*- coding:utf-8 -*-
# @author: qianli
# @file: maxCount.py
# @time: 2019/08/21
def maxCount(m, n, ops):
    if not ops:
        return m * n
    if type(ops[0]) is int:
        return ops[0] * ops[1]
    else:
        a = min(map(lambda x: x[0], ops))
        b = min(map(lambda x: x[1], ops))
        return a * b




print(maxCount(3,3,[2,2]))

