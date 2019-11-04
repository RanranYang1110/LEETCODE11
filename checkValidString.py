#-*- coding:utf-8 -*-
# @author: qianli
# @file: checkValidString.py
# @time: 2019/09/23
def checkValidString(s: str) -> bool:
    if len(s) == 0:
        return True
    left, mid, right = 0, 0, 0
    for i in range(len(s)):
        if s[i] == '(': left += 1
        if s[i] == ')': right += 1
        if s[i] == '*': mid += 1
        if left + mid < right: return False
    if left == right: return True
    if left < right and left + mid >= right: return True
    if left > right and left <= right + mid: return True
    return False
s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"

print(checkValidString(s))