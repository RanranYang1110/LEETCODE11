#-*- coding:utf-8 -*-
# @author: qianli
# @file: productExceptSelf.py
# @time: 2019/09/16
def productExceptSelf(nums):
    '''给定长度为n的整数数组nums,其中n>1,返回输出数组output。
    其中，output[i]等于nums中除nums[i]之外其余各元素的乘积'''
    '''示例：输入[1,2,3,4] 输出[24, 12, 8, 6]'''
    N = len(nums)
    res = [0] * N
    res[0] = nums[0]
    for i in range(1, N):
        res[i] = res[i-1] * nums[i]
    inter = 1
    for j in range(N-1, 0, -1):
        res[j] = res[j-1] * inter
        inter *= nums[j]
    res[0] = inter
    return res
nums = [1,2,3,4]
print(productExceptSelf(nums))


