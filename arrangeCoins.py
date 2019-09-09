#-*- coding:utf-8 -*-
# @author: qianli
# @file: arrangeCoins.py
# @time: 2019/08/07
def arrangeCoins(n):
    minValue = 1
    maxValue = n
    if n == 1:
        return 1
    else:
        while maxValue - minValue > 1:
            midValue = int((minValue + maxValue) / 2)
            if  midValue * (midValue + 1) / 2 - n < 0:
                minValue = midValue
            elif midValue * (midValue + 1) / 2 - n > 0:
                maxValue = midValue
            else:
                minValue = midValue
                maxValue = midValue
        return minValue
print(arrangeCoins(5))