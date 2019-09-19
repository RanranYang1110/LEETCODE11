#-*- coding:utf-8 -*-
# @author: qianli
# @file: findDisappearedNumbers.py
# @time: 2019/09/17
def findDisappearedNumbers(nums):
    N = len(nums)
    data = list(set(nums))
    data1 = []
    for i in range(1, N+1):
        data1.append(i)
    for i in range(len(data)):
        data1.remove(data[i])
    return data1
def findDisappearedNumbers2(nums):
    N = len(nums)
    data = list(set(nums))
    for i in range(0, N):
        data[data[i]] = data[data[i]] * -1
    return data

nums = [4, 3, 2, 7, 8, 2, 3, 1]
data22a = findDisappearedNumbers2(nums)