#-*- coding:utf-8 -*-
# @author: qianli
# @file: fourSumCount.py
# @time: 2019/11/11
def fourSumCount(A, B, C, D):
    '''四数相加'''

    n = len(A)
    dict_a = {}
    for d1 in A:
        for d2 in B:
            value = 0 - d1 - d2
            if value in dict_a:
                dict_a[value] += 1
            else:
                dict_a[value] = 1
    count = 0
    for d3 in C:
        for d4 in D:
            value2 = d3 + d4
            if value2 in dict_a:
                count += dict_a[value2]
    return count
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]

# A = [-1, -1]
# B = [-1, 1]
# C = [-1, 1]
# D = [1, -1]
print(fourSumCount(A, B, C, D))