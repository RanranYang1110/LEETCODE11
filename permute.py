#-*- coding:utf-8 -*-
# @author: qianli
# @file: permute.py
# @time: 2019/09/12
def permute(nums):
    '''全排列'''
    res = []
    def backtrack(nums, tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
    backtrack(nums, [])
    return res

print(permute([1,2,3]))