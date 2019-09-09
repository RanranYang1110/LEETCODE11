#-*- coding:utf-8 -*-
# @author: qianli
# @file: twoSum.py
# @time: 2019/08/07
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict_a = {}
    for i in range(len(numbers)):
        x = target - numbers[i]
        if numbers[i] not in dict_a:
            dict_a[x] = i
        else:
            return [dict_a[numbers[i]], i]

numbers = [7, 11, 2, 15]
targets = 9
print(twoSum(numbers, targets))