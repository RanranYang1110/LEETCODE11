#-*- coding:utf-8 -*-
# @author: qianli
# @file: guessNum.py
# @time: 2019/08/07
def guess(m):
    value = 6
    if  m == value:
        return 0
    elif m < value:
        return -1
    else:
        return 1

#%%
def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """
    minValue = 1
    maxValue = n
    if guess(minValue) == 0:
        return minValue
    elif guess(maxValue) == 0:
        return maxValue
    else:
        while maxValue - minValue > 1:
            midValue = int((minValue + maxValue) / 2)
            if guess(midValue) == -1:
                minValue = midValue
            elif guess(midValue) == 1:
                maxValue = midValue
            else:
                minValue = midValue
                maxValue = midValue
        return midValue
print(guessNumber(10))