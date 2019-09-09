#-*- coding:utf-8 -*-
# @author: qianli
# @file: maxProfit1.py
# @time: 2019/09/04
def maxProfit(prices):
    pro = 0
    for i in range(1, len(prices)):
        v = prices[i] - prices[i - 1]
        pro += v if v > 0 else 0
    return pro
prices = [7,3,4,3,6,7]
prices = []
print(maxProfit(prices))
