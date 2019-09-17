#-*- coding:utf-8 -*-
# @author: qianli
# @file: longestPalindrome1.py
# @time: 2019/09/17
def longestPalindrome(s):
    dict1 = {}
    for i in range(len(s)):
        if s[i] in dict1:
            dict1[s[i]] += 1
        else:
            dict1[s[i]] = 1
    values = list(dict1.values())
    sum1 = 0
    for value in list(dict1.values()):
        if value % 2 == 0:
            sum1 += value
        else:
            sum1 += value - 1
            k = 1
    return sum1 + k
s = 'abccccdd'
dict1 = longestPalindrome(s)