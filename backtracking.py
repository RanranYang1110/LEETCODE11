#-*- coding:utf-8 -*-
# @author: qianli
# @file: backtracking.py
# @time: 2019/09/21
def subsets_recursive(nums):
    lst = []
    result = []
    subsets_recursive_helper(result, lst, nums, 0)
    return result

def subsets_recursive_helper(result, lst, nums, pos):
    result.append(lst[:])
    for i in range(pos, len(nums)):
        lst.append(nums[i])
        subsets_recursive_helper(result, lst, nums, i + 1)
        lst.pop()


def subsets(nums):
    res = []
    n = len(nums)
    def helper(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            helper(j + 1, tmp + [nums[j]])
    helper(0, [])
    return res

# nums = ['a','b','c']
# print(subsets_recursive(nums))
nums = [1,2,3]
print(subsets(nums))
