#-*- coding:utf-8 -*-
# @author: qianli
# @file: nextGreatestLetter.py
# @time: 2019/08/08
def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    letters = sorted(list(set(letters + [target])))
    if letters[-1] == target:
        return letters[0]
    else:
        return letters[letters.index(target) + 1]

letters = ['c', 'f', 'j']
target = 'c'
print(nextGreatestLetter(letters, target))