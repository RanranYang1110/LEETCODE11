#-*- coding:utf-8 -*-
# @author: qianli
# @file: letterCount.py
# @time: 2019/11/10
def letterCount(s):
    '''统计字母数'''
    freq = {}
    for piece in s:
        word = ''.join(c for c in piece if c.isalpha())
        if word:
            freq[word] = 1 + freq.get(word, 0)
    max_word = ''
    max_count = 0
    for (w, c) in freq.items():
        if c > max_count:
            max_word = w
            max_count = c
    return max_word, max_count

s = "Hello World How are you I am fine thank you and you"
print(letterCount(s))
