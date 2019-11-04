#-*- coding:utf-8 -*-
# @author: qianli
# @file: generateParenthesis.py
# @time: 2019/09/22
def generateParenthesis(n):
    '''生成有效的括号'''
    def generate(prefix, left, right, parens=[]):
        if right == 0: parens.append(prefix)
        if left > 0: generate(prefix + '(', left-1, right)
        if right > left: generate(prefix + ')', left, right-1)
        return parens
    return generate('', n, n)
generateParenthesis(2)