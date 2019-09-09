#-*- coding:utf-8 -*-
# @author: qianli
# @file: convertToTitle.py
# @time: 2019/08/20

def convertToTitle(n):
    values = []
    for i in range(65, 91):
        values.append(chr(i))
    keys = []
    for i in range(1,27):
        keys.append(i)
    dict_a = dict(zip(keys, values))
    res_a = ''
    if n % 26 == 0:
        cs = n // 26
        if cs == 1:
            return 'Z'
        else:
            return dict_a[cs-1] + 'Z'
    else:
        while n > 26:
            mm = n % 26
            n = n // 26
            res_a += dict_a[mm]
        res_a += dict_a[n]
        return res_a[::-1]
    # print(res_a)
print(convertToTitle(701))
