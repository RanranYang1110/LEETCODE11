#-*- coding:utf-8 -*-
# @author: qianli
# @file: merge.py
# @time: 2019/09/04
def merge(nums1, m, nums2, n):
    if nums2 == '':
        return nums1[:m]
    elif nums1 == '':
        return nums2[:n]
    else:
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        nn = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nn.append(nums1[i])
                i += 1
            else:
                nn.append(nums2[j])
                j += 1
        if i == m:
            while j < n:
                nn.append(nums2[j])
                j += 1
        elif j == n:
            while i < m:
                nn.append(nums1[i])
                i += 1
        return nn
def merge2(nums1, m, nums2, n):
    i, j = 0, 0
    while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i + 1:m + 1] = nums1[i:m]
                nums1[i] = nums2[j]
                m += 1
                j += 1
                i += 1
    nums1[i:m + n] = nums2[j:n]
    return nums1[:m + n]
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge2(nums1, 3, nums2, 3))

nums1 = [2,0]
nums2 = [1]
print(merge2(nums1, 1, nums2, 1))



