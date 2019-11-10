#-*- coding:utf-8 -*-
# @author: qianli
# @file: numJewelsInStones_bf.py
# @time: 2019/11/10
def numJewelsInStones_bf(J, S):
    '''宝石和石头'''
    res = 0
    JJ = set(J)
    for stone in S:
        if stone in JJ:
           res += 1
    return res
J = 'aA'
S = 'aAAbbbb'
J = 'z'
S = 'ZZ'
print(numJewelsInStones_bf(J, S))