#-*- coding:utf-8 -*-
# @author: qianli
# @file: intersect.py
# @time: 2019/11/12
def intersect(nums1, nums2):
    '''
    : 求两个数组的交集
    :param nums1: 数组1
    :param nums2: 数组2
    :return:
    '''
    n1, n2 = len(nums1), len(nums2)
    dict1 = {}
    if n1 > n2:
        n1, n2 = n2, n1
    for num in nums1:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    res = []
    for num2 in nums2:
        if num2 in dict1 and dict1[num2] > 0:
            res.append(num2)
            dict1[num2] -= 1
    return res

nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))