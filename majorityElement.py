#-*- coding:utf-8 -*-
# @author: qianli
# @file: majorityElement.py
# @time: 2019/08/21
def majorityElement(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        res_dict = {}
        N = len(nums)
        for i in nums:
            if i not in res_dict:
                res_dict[i] = 1
            else:
                res_dict[i] += 1
            if res_dict[i] > N/2:
                return i

nums = [2, 2, 1,1,1,2,2,2]
print(majorityElement(nums))