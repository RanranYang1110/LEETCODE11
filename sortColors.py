#-*- coding:utf-8 -*-
# @author: qianli
# @file: sortColors.py
# @time: 2019/09/19
def sortColors(nums):
    dict1 = {0:0, 1:0, 2:0}
    for i in nums:
        dict1[i] += 1
    res = [0] * dict1[0] + [1] * dict1[1] + [2] * dict1[2]
    return res

def sortColors1(nums):
    '''初始化0的最右边界，P0=0;
        初始化2的最左边界，P2=N-1,'''
    p0 = 0
    cur = 0
    p2 = len(nums) - 1
    while cur <= p2:
        if nums[cur] == 0:
            nums[p0], nums[cur] = nums[cur], nums[p0]
            p0 += 1
            cur += 1
        elif nums[cur] == 2:
            nums[p2], nums[cur] = nums[cur], nums[p2]
            p2 -= 1
        else:
            cur += 1



nums = [2, 0, 2, 1, 1, 0]
res = sortColors1(nums)