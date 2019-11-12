#-*- coding:utf-8 -*-
# @author: qianli
# @file: increasingTriplet.py
# @time: 2019/11/12
def increasingTriplet(nums):
    '''递增的三元子序列'''
    # 给定一个未排序的数组，判断这个数组中是否存在长度未3的递增子序列
    count1 = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count1 += 1
            if count1 == 3:
                return True
        else:
            count1 = 1
    return False

def increasingTriplet(self, nums: [int]) -> bool:
    if len(nums) < 3:
        return False

    win = [nums[0]]
    for num in nums:
        if num > win[-1]:
            win.append(num)
            if len(win) >= 3:
                return True
        else:
            i = len(win) - 1
            while i > 0 and win[i - 1] >= num:
                i -= 1
            win[i] = num
    return False

nums = [1,2,1,4,3]
nums = [5, 1, 5, 5, 3, 5, 4]
print(increasingTriplet(nums))