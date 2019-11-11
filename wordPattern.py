#-*- coding:utf-8 -*-
# @author: qianli
# @file: wordPattern.py
# @time: 2019/11/10
def wordPattern(pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

pattern = 'abba'
str = 'dog dog dog dog'
print(wordPattern(pattern, str))