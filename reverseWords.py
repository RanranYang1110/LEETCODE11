#-*- coding:utf-8 -*-
# @author: qianli
# @file: reverseWords.py
# @time: 2019/09/06
def reverseWords(s):
    ss = s.split(' ')
    ii = ''
    for i in ss:
        ii = ii + i[::-1] + ' '
    return ii

s = "helloo world"
print(reverseWords(s))