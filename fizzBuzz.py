#-*- coding:utf-8 -*-
# @author: qianli
# @file: fizzBuzz.py
# @time: 2019/09/05
def fizzBuzz(n):
    aa = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res = 'FizzBuzz'
        elif i % 3 == 0:
            res = 'Fizz'
        elif i % 5 == 0:
            res = 'Buzz'
        else:
            res = str(i)
        aa.append(res)
    return aa

print(fizzBuzz(15))