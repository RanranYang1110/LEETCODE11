#-*- coding:utf-8 -*-
# @author: qianli
# @file: subsets.py
# @time: 2019/09/16
def subsets(nums):
    '''给定一组不含重复元素的整数数组nums，返回该数据所有可能的子集'''
    '''迭代方法'''
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res

def subsets1(nums):
    '''回溯算法'''
    res = []
    n = len(nums)
    def helper(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            helper(j+1, tmp + [nums[j]])
    helper(0, [])
    return res
nums = [1, 2, 3]
mm = subsets(nums)
mm2 = subsets1(nums)