#-*- coding:utf-8 -*-
# @author: qianli
# @file: isugly.py
# @time: 2019/08/20
def isUgly(num):
    if num < 1:
        return False
    elif num == 1:
        return True
    else:
        mm = [2, 3, 5]
        while num != 1:
            if num %2 == 0:
                num /=2
            elif num % 3 == 0:
                num /=3
            elif num % 5 == 0:
                num /= 5
            else:
                return False
        return True
num = 6
print(isUgly(num))