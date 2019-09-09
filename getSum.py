#-*- coding:utf-8 -*-
# @author: qianli
# @file: getSum.py
# @time: 2019/08/27
def getSum(a, b):
    MASK = 0x100000000
    # 整型最大值
    MAX_INT = 0x7FFFFFFF
    MIN_INT = MAX_INT + 1
    or1 = a ^ b #异或操作，表示只有一个为1
    and1 = a & b #与操作，表示两个数值都为1，存在进位
    while b != 0:
        # 计算进位
        carry = (a & b) << 1
        # 取余范围限制在 [0, 2^32-1] 范围内
        a = (a ^ b) % MASK
        b = carry % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

