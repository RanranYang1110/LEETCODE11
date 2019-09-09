#-*- coding:utf-8 -*-
# @author: qianli
# @file: peakIndexInMountainArray.py
# @time: 2019/08/08

def peakIndexInMountainArray(A):
    """
    :type A: List[int]
    :rtype: int
    """
    if len(A) == 3:
        return 1
    else:
        minIndex = 0
        maxIndex = len(A)
        while maxIndex > minIndex :
            midIndex = (maxIndex + minIndex) // 2
            if A[midIndex] > A[midIndex -1] and A[midIndex] > A[midIndex + 1]:
                return midIndex
                break
            elif A[midIndex] < A[midIndex - 1]:
                maxIndex= midIndex
            else:
                minIndex = midIndex
A = [40, 48, 61, 75, 100, 99, 98, 39, 30, 10]
print(peakIndexInMountainArray(A))