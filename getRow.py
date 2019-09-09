#-*- coding:utf-8 -*-
# @author: qianli
# @file: getRow.py
# @time: 2019/08/18
def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]
    else:
        res = []
        for i in range(1, rowIndex + 1):
            temp = [1] * (i + 1)
            res.append(temp)
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res[rowIndex]

print(getRow(0))