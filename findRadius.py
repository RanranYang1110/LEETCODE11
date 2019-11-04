#-*- coding:utf-8 -*-
# @author: qianli
# @file: findRadius.py
# @time: 2019/09/23
def findRadius(house, heaters):
    heaters = sorted(heaters)
    res = 0
    def select(nums, target):
        if len(nums) == 1:
            return [nums[0], nums[0]]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target: left = mid
            elif nums[mid] == target: return [nums[mid], nums[mid]]
            else: right = mid
        return nums[left], nums[right]
    def dis(left, right, num):
        return min(abs(num - left), abs(num - right))
    for i in house:
        left, right = select(heaters, i)
        res = max(dis(left, right, i), res)
    return res
house = [1, 12, 23, 34]
heaters = [24, 12]
# house = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
# heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
print(findRadius(house, heaters))