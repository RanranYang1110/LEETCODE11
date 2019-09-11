#-*- coding:utf-8 -*-
# @author: qianli
# @file: multiply.py
# @time: 2019/09/11
def multiply(num1, num2):
    if len(num1) > len(num2):
        a, b = num1, num2
    else:
        a, b = num2, num1
    sum1 = 0
    for i in range(len(b)):
        sum1 += (int(b[i]) * 10 ** (len(b) - i  - 1)) * int(a)
    return str(sum1)
num1, num2 = '10', '20'
print(multiply(num1, num2))
print(int(num1) * int(num2))