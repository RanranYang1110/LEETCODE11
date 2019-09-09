#-*- coding:utf-8 -*-
# @author: qianli
# @file: intersection.py
# @time: 2019/08/07
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    res = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            res.append(nums1[i])
    return res
n1 = [1,2,2,1]
n2 = [2,2]
print(intersection(n1, n2))
#%%
def intersect(nums1, nums2):
    res = []
    if len(nums1) <= len(nums2):
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.pop(nums2.index(nums1[i]))
        return res
    else:
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                res.append(nums2[i])
                nums1.pop(nums1.index(nums2[i]))
        return res
n1 = [2,1]
n2 = [1,2]
print(intersect(n1, n2))