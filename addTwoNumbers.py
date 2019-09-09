#-*- coding:utf-8 -*-
# @author: qianli
# @file: addTwoNumbers.py
# @time: 2019/09/06
def threeSum(nums):
    nums1 = sorted(nums)
    res = []
    for i in range(0, len(nums)-2):
        if nums1[i] > 0: break
        if i >0 and nums1[i] == nums1[i-1]: continue
        j = i + 1 #左指针
        k = len(nums) -1
        while j < k:
            s = nums1[i] + nums1[j] + nums1[k]
            if s == 0:
                res.append([nums1[i], nums1[j], nums1[k]])
                j += 1
                k -= 1
                while j < k and nums1[j] == nums1[j-1]: j += 1
                while j < k and nums1[k] == nums1[k+1]: k -= 1
            elif  s > 0:
                k -= 1
                while j < k and nums1[k] == nums1[k+1]: k -= 1
            else:
                j += 1
                while j < k and nums1[j] == nums1[j-1]: j += 1
    return res
nums = [1, -1, -1, 0]
print(threeSum(nums))