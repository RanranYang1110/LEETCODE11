#-*- coding:utf-8 -*-
# @author: qianli
# @file: test_fun.py
# @time: 2019/09/18
def sum1(a):
    return a + 1

a = 5
for _ in range(5):
    a = sum1(a)
print('a=', a)


b = 5
while b < 10:
    b = sum1(b)
print('b=',b)

