#-*- coding:utf-8 -*-
# @author: qianli
# @file: Subset.py
# @time: 2019/09/01
def subsets(nums):
    '''搜索字符串中的所有子集'''
    result = [[]]
    for num in nums:
        for element in result[:]:
            x = element[:]
            x.append(num)
            result.append(x)
    return result

nums = [1,2,3]
print(subsets(nums))




def subset_recursive_helper(result, lst, nums, pos):
    result.append(lst[:])
    for i in range(pos, len(nums)):
        lst.append(nums[i])
        subset_recursive_helper(result, lst, nums, i+1)
        lst.pop()

def subsets_recursive(nums):
    lst = []
    result = []
    subset_recursive_helper(result, lst, nums, 0)
    return result
nums = ['a','b','c']
print(subsets_recursive(nums))
