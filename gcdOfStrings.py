#-*- coding:utf-8 -*-
# @author: qianli
# @file: gcdOfStrings.py
# @time: 2019/08/13
def gcdOfStrings(str1, str2):
    if len(str1) >= len(str2):
        l1 = str2
        l2 = str1
    else:
        l1 = str1
        l2 = str2
    for i in range(len(l1)):

