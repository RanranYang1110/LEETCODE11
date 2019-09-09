#-*- coding:utf-8 -*-
# @author: qianli
# @file: maxProfit.py
# @time: 2019/08/13
def maxProfit(prices):
    if len(prices) <= 0:
        return 0
    else:
        minValue = prices[0]
        maxPro = 0
        for i in range(1, len(prices)):
            maxPro = max(prices[i] - minValue, maxPro)
            minValue = min(minValue, prices[i])
        return maxPro
prices = [7,1, 5, 3, 6, 4]
print(maxProfit(prices))