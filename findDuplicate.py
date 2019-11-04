#-*- coding:utf-8 -*-
# @author: qianli
# @file: findDuplicate.py
# @time: 2019/09/19
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1

def findDuplicate1(nums):
    n = len(nums)
    low = 1
    high = len(nums) -1
    while low < high:
        mid = low + (high - low) // 2
        count = 0
        for i in nums:
            if i <= mid:
                count += 1
        if count <= mid:
            low = mid + 1
        else:
            high = mid
    return low
nums = [3, 5, 6, 3, 1, 4, 2]
print(findDuplicate1(nums))