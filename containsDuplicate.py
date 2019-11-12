#-*- coding:utf-8 -*-
# @author: qianli
# @file: containsDuplicate.py
# @time: 2019/11/12
def containsDuplicate(nums):
    data = {}
    for num in nums:
        if num not in data:
            data[num] = 1
        else:
            return True
    return False

nums = []
print(containsDuplicate(nums))