#-*- coding:utf-8 -*-
# @author: qianli
# @file: maxArea.py
# @time: 2019/09/11
def maxArea(height):
    '''盛最多水的容器'''
    i, j, res = 0, len(height) - 1, 0
    while i < j:
        res1 = (j - i) * min(height[i], height[j])
        if  res1 > res:
            res = res1
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res

hh = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(hh))