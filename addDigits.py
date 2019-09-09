#-*- coding:utf-8 -*-
# @author: qianli
# @file: addDigits.py
# @time: 2019/08/20

def divv(num):
    data = []
    while num >= 10:
        res = num % 10
        num = num // 10
        data.append(res)
    data.append(num)
    return data

def addDigits(num):
    data = divv(num)
    while sum(data) >= 10:
        data = divv(sum(data))
    return sum(data)
num = 10
print(addDigits(num))