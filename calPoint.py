#-*- coding:utf-8 -*-
# @author: qianli
# @file: calPoint.py
# @time: 2019/11/04
def calPoint(s):
    '''棒球比赛分数计算'''
    stack = []
    for num in s:
        if num == 'C':
            stack.pop()
        elif num == 'D':
            stack.append(int(stack[-1] * 2))
        elif num == '+':
            stack.append(int(stack[-1]) + int(stack[-2]))
        else:
            stack.append(int(num))
    return sum(stack)

s = ['5','2','C','D','+']
print(calPoint(s))

