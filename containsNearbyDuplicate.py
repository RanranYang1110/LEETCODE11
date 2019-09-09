#-*- coding:utf-8 -*-
# @author: qianli
# @file: containsNearbyDuplicate.py
# @time: 2019/09/06
def containsNearbyDuplicate(nums, k):
    lookup = {}
    if len(set(nums)) == len(nums):
        return False
    for idx, num in enumerate(nums):
        if num in lookup and idx - lookup[num] <=k:
            return True
        lookup[num] = idx
    return False