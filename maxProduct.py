#-*- coding:utf-8 -*-
# @author: qianli
# @file: maxProduct.py
# @time: 2019/11/12
def maxProduct(nums):
    '''
    : 给定一个整数数组nums, 找出一个序列中乘积最大的连续子序列（该序列至少一个一个数）
    :param nums:
    :return:
    '''
    if len(nums) == 1:
        return nums[0]
    result, max_1, min_1 = nums[0], nums[0], nums[0]
    for i in range(1,len(nums)):
        temp_max = max_1
        temp_min = min_1
        # max_n = max(nums[i], max(temp_max * nums[i], temp_min * nums[i]))
        # min_n = min(nums[i], min(temp_min * nums[i], temp_max * nums[i]))
        max_1 = max(nums[i], temp_max * nums[i], temp_min * nums[i])
        min_1 = min(nums[i], temp_max * nums[i], temp_min * nums[i])
        result = max(result, max_1)
    return result
nums = [2, 3, -2, 4]
nums = [2, 3, -2, 4, -5,1]
print(maxProduct(nums))