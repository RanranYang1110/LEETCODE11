#-*- coding:utf-8 -*-
# @author: qianli
# @file: majorityElement2.py
# @time: 2019/08/21
def majorityElement(nums):
    data = []
    if len(nums) == 1:
        data.append(nums[0])
        return data
    else:
        res_dict = {}
        N = len(nums)
        for i in nums:
            if i not in res_dict:
                res_dict[i] = 1
            else:
                res_dict[i] += 1
            if res_dict[i] > N/3:
                data.append(i)
        return list(set(data))
nums = [1]
data = majorityElement(nums)
# print(majorityElement(nums))