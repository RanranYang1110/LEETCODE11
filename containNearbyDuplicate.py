#-*- coding:utf-8 -*-
# @author: qianli
# @file: containNearbyDuplicate.py
# @time: 2019/08/18
def containsNearbyDuplicate(nums, k):
    if len(nums) < k:
        return False
    else:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    return True
        return False
    #%%

def containsNearbyDuplicate1(nums, k):
    dict = {}
    for  i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = i
        else:
            if i - dict[nums[i]] <= k:
                return True
    return False
nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate1(nums, k))