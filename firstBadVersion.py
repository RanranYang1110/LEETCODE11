#-*- coding:utf-8 -*-
# @author: qianli
# @file: firstBadVersion.py
# @time: 2019/08/07
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    minIndex = 1
    maxIndex = n
    while maxIndex - minIndex > 1:
        midIndex = int(minIndex + maxIndex) / 2
        if isBadVersion(midIndex) == True:
            minIndex = midIndex
        else:
            maxIndex = midIndex
    return maxIndex