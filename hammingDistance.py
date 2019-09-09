#-*- coding:utf-8 -*-
# @author: qianli
# @file: hammingDistance.py
# @time: 2019/09/02
def hammingDistance(x, y):
    '''计算两个整数之间的汉明距离'''
    return bin(x ^ y).count('1')