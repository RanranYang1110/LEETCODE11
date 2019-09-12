#-*- coding:utf-8 -*-
# @author: qianli
# @file: search.py
# @time: 2019/09/12

# def find_changePos(nums):
#     l = 0
#     r = len(nums)
#     if len(nums) == 2:
#         if nums[0] > nums[1]:
#             return 0
#         else:
#             return 1
#     if nums[l] < nums[r-1]:
#         return 0
#     while l < r :
#         mid = (l + r) // 2
#         if nums[mid] > nums[mid + 1]:
#             return mid
#         else:
#             if nums[0] > nums[mid]:
#                 r = mid
#             else:
#                 l = mid
#
#     return mid
#
# def search(nums, target):
#     if len(nums) == 0:
#         return -1
#     if len(nums) == 1 and nums[0] == target:
#         return 0
#     if len(nums) == 1 and nums[0] != target:
#         return -1
#     pos = find_changePos(nums)
#     if pos != 0 and nums[pos] < target:
#         return -1
#     if nums[pos] >= target and nums[0] <= target:
#         l = 0
#         r = pos
#     else:
#         l = pos
#         r = len(nums) - 1
#     while l < r:
#         mid = (l + r) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             r = mid - 1
#         else:
#             l = mid + 1
#     return -1


def search(nums, target):
    def find_rotate_index(left, right):
        if nums[left] < nums[right]:
            return 0

        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1

    def search(left, right):
        """
        Binary search
        """
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            else:
                if target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
        return -1

    n = len(nums)

    if n == 0:
        return -1
    if n == 1:
        return 0 if nums[0] == target else -1

    rotate_index = find_rotate_index(0, n - 1)

    # if target is the smallest element
    if nums[rotate_index] == target:
        return rotate_index
    # if array is not rotated, search in the entire array
    if rotate_index == 0:
        return search(0, n - 1)
    if target < nums[0]:
        # search on the right side
        return search(rotate_index, n - 1)
    # search on the left side
    return search(0, rotate_index)
nums = [1,3]
# print(find_changePos(nums))
print(search(nums, 3))
