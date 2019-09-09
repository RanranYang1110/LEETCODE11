#-*- coding:utf-8 -*-
# @author: qianli
# @file: PlusOne.py
# @time: 2019/08/26
def plusOne(digits):
    '''给定一个由整数组成的非空数据所表示的非负整数，在该数的基础上加1
    输入：[1,2,3]
    输出：[1,2,4]
    '''
    if len(digits)==1 and digits[0] == 9:
        return [1, 0]
    if 9 not in digits:
        data = digits
        data[-1] = data[-1] + 1
        return data
    else:
        data = digits
        for i in range(len(digits)):
            j = len(digits)- 1 - i
            data[j] += 1
            data[j] %= 10
            if (data[j] != 0):
                return data

        data1 = [0] * (len(digits)+1)
        data1[0] = 1
        return data1
digits = [1, 9]

print(plusOne([1,9,9]))
