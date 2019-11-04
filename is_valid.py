#-*- coding:utf-8 -*-
# @author: qianli
# @file: is_valid.py
# @time: 2019/10/31
# from LinkedList import LinkedList
# from LinkedList import Node
# from ArrayStack import ArrayStack
'''用堆栈的方式判断是否为有效的括号'''
def isValid(s):
    stack = []
    for c in s:
        if (c == '(' or c == '[' or c == '{'):
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if ( (c == ')' and stack[-1] == '(') or
                 (c == ']' and stack[-1] == '[') or
                 (c == '}' and stack[-1] == '{')):
                stack.pop()
            else:
                return False
    return len(stack) == 0
s = '{(})'
print(isValid(s))