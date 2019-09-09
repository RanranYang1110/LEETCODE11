#-*- coding:utf-8 -*-
# @author: qianli
# @file: climbStairs.py
# @time: 2019/08/13
def climbStairs(n):
    f = [1, 2]
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    return f[n-1]
print(climbStairs(4))