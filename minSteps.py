#-*- coding:utf-8 -*-
# @author: qianli
# @file: minSteps.py
# @time: 2019/09/26
def minSteps(height):
    def minStepHelper(height, left, right, h):
        if left >= right:
            return 0
        m = left
        for i in range(left, right):
            if height[i] < height[m]:
                m = i
        return min(right-left, minStepHelper(height, left, m, height[m]) + minStepHelper(height, m+1, right, height[m]) + height[m]-h)

    return minStepHelper(height, 0, len(height), 0)

height = [3, 1, 2, 5, 1]
height = [3, 3, 3, 15, 3]
minSteps(height)