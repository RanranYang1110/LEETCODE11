#-*- coding:utf-8 -*-
# @author: qianli
# @file: titleToNumber.py
# @time: 2019/08/20
def titleToNumber(s):
    values = []
    for i in range(65, 91):
        values.append(chr(i))
    keys = []
    for i in range(1,27):
        keys.append(i)
    dict_a = dict(zip(values, keys))
    mm = 0
    N = len(s)
    for i in range(N):
        mm += 26 ** (N - i -1) * dict_a[s[i]]
    return mm

def titleToNumber2(s):
    dict_a = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G': 7, 'H': 8, 'I':9, 'J': 10, 'K':11, 'L':12, 'M':13,
              'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T': 20, 'U': 21, 'V':22, 'W': 23, 'X':24, 'Y':25, 'Z':26}
    m = 0
    N = len(s)
    for i in range(N):
        m += dict_a[s[i]] * 26 ** (N - 1 - i)
    return m
print(titleToNumber2('Y'))
# 'AB' -- 28
#'AAA' -- 703