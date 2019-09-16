#-*- coding:utf-8 -*-
# @author: qianli
# @file: grayCode.py
# @time: 2019/09/16
def grayCode(n):
    '''生成格雷码
    G(n)左边加0，得到G'(n)
    G(n)倒叙，左边加一，得到H'(n)
    G(n+1) = G'(n) 并 H'(n)
    '''
    res = [0]
    for i in range(n):
        for j in range(len(res) - 1, -1 , -1):
            res.append(res[j] ^ (1 << i))
    '''<< 指的是位运算 ^ 为异或运算'''
    return res
n = 0
print(grayCode(n))
