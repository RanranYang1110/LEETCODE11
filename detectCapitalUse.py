#-*- coding:utf-8 -*-
# @author: qianli
# @file: detectCapitalUse.py
# @time: 2019/09/18
def detectCapitalUse(word):

    if word.isupper() or word.islower() or word.istitle():
        return True
    elif word[0].isupper() and word[1:].islower():
        return True
    return False

word = 'FlagG'
print(detectCapitalUse(word))