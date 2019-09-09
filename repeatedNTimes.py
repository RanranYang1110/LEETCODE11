#-*- coding:utf-8 -*-
# @author: qianli
# @file: repeatedNTimes.py
# @time: 2019/08/20
def repeatedNTimes(A):
    N = len(A) / 2
    list1 = list(set(A))
    return int((sum(A) - sum(list1))/ (N-1))
A = [5, 1, 5, 2, 5, 3, 5, 4]
print(repeatedNTimes(A))