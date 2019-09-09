#-*- coding:utf-8 -*-
# @author: qianli
# @file: removeElement.py
# @time: 2019/08/12
def removeElement(nums, val):
    if len(nums) == 0:
        return 0
    elif val not in nums:
        return len(nums)  #注意这里 [2],3
    else:
        m = 0
        for i in range(len(nums)):
            if nums[m] == val:
                nums.append(val)
                nums.pop(m)
            else:
                m += 1
        return len(nums[:m])

nums = []
val = 0
print(removeElement(nums, val))
