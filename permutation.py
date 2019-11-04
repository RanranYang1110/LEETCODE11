#-*- coding:utf-8 -*-
# @author: qianli
# @file: permutation.py
# @time: 2019/09/21
def perm(result, nums):
    '''全排列'''
    if (len(nums)) == 0:
        print(result)
    for i in range(len(nums)):
        perm(result + str(nums[i]), nums[0:i]+nums[i+1:])


def permute(nums):
    '''全排列'''
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(nums)):
                new_perms.append(perm[:i] + [n] + perm[i:])
        perms = new_perms
    return perms
nums = [1,2,3]
perm('',nums)
mm = permute(nums)