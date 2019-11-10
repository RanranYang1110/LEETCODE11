#-*- coding:utf-8 -*-
# @author: qianli
# @file: singleNumber.py
# @time: 2019/11/10
def singleNumber(nums):
    '''
    :仅出现一次的数字
    :param nums:
    :return:
    '''
    dict = {}
    for num in nums:
        if num in dict:
            del dict[num]
        else:
            dict[num] = 0
    return list(dict.keys())[0]

nums = [4,1,2,2,1]
print(singleNumber(nums))