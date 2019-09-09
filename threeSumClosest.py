#-*- coding:utf-8 -*-
# @author: qianli
# @file: threeSumClosest.py
# @time: 2019/09/09
def threeSumClosest(nums, target):
    nums1 = sorted(nums)
    div = abs(nums1[0]+ nums1[1] + nums1[2] - target)
    for i in range(0, len(nums)-2):
        if i > 0 and nums1[i] == nums1[i - 1]: continue
        j, k = i + 1, len(nums) -1
        while j < k:
            ss = nums1[i] + nums1[j] + nums1[k] - target
            if abs(ss) < div:
                res = nums1[i] + nums1[j] + nums1[k]
                div = abs(ss)
            if ss  == 0:
                return target
            elif ss > 0:
                k -= 1
                while j < k and nums1[k] == nums1[k+1]: k -= 1
            else:
                j += 1
                while j < k and nums1[j] == nums1[j-1]: j += 1
    return res

nums = [-1, 2, 1, -4]
traget = 1
print(threeSumClosest(nums, traget))