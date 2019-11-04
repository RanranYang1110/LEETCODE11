#-*- coding:utf-8 -*-
# @author: qianli
# @file: findPeakElement.py
# @time: 2019/09/23
def findpeakElement(nums):
    left, right = 0, len(nums)-1
    # nums[-1] = float(inf)
    # nums[len(nums)] = float('inf')
    return peak_helper(nums, left, right)
def peak_helper(alist, start, end):
    if start == end:
        return start
    if start + 1 == end:
        if alist[start] > alist[end]:
            return start
        return end
    mid = (start + end)//2
    if alist[mid] > alist[mid - 1] and alist[mid] > alist[mid + 1]:
        return mid
    elif alist[mid] > alist[mid-1] and alist[mid] < alist[mid + 1]:
        return peak_helper(alist, mid + 1, end)
    else:
        return peak_helper(alist, start, mid - 1)

nums = [1,2,3,1]
print(findpeakElement(nums))

