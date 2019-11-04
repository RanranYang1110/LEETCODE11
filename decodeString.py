#-*- coding:utf-8 -*-
# @author: qianli
# @file: decodeString.py
# @time: 2019/11/04
def decodeString(s):
    stack = []
    stack.append(["", 1])
    num = ""
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == '[':
            stack.append(["", int(num)])
            num = ""
        elif ch == ']':
            st, k = stack.pop()
            stack[-1][0] += st * k
        else:
            stack[-1][0] += ch
    return stack[0][0]

s = "3[a]2[bc]"
print(decodeString(s))