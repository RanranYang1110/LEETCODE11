#-*- coding:utf-8 -*-
# @author: qianli
# @file: nextGreaterElement.py
# @time: 2019/09/17
def nextGreaterElement(nums1, nums2):
    res = []
    for i in nums1:
        data = nums2.index(i)
        mindata = -1
        for j in range(data+1,len(nums2)):
            if nums2[j] > i:
                mindata = nums2[j]
                break
        res.append(mindata)
    return res
nums1 = [4,1,2]
nums2 = [1,3,4,2]
res = nextGreaterElement(nums1, nums2)