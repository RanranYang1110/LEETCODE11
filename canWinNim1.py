#-*- coding:utf-8 -*-
# @author: qianli
# @file: canWinNim1.py
# @time: 2019/09/16
def canWinNim(n):
    '''Nim游戏，计算是否能够胜利'''
    return n%4 != 0
print(canWinNim(4))