#-*- coding:utf-8 -*-
# @author: qianli
# @file: countPrimes.py
# @time: 2019/08/23
def countPrimes(n):
    if n < 3:
        return 0
    else:
        output = [1] * n
        output[0], output[1] = 0, 0
        for i in range(2, int(n ** 0.5) + 1):
            if output[i] == 1:
                output[i * i : n : i] = [0] * len(output[i * i : n : i])
    return sum(output)
print(countPrimes(10))
