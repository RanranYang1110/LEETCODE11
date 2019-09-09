#-*- coding:utf-8 -*-
# @author: qianli
# @file: getNums.py
# @time: 2019/08/18
def generate(numRows):
    res = []
    for i in range(numRows):
        temp = [1] * (i + 1)
        res.append(temp)
        for j in range(1, i):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res

print(generate(0))
