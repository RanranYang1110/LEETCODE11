#-*- coding:utf-8 -*-
# @author: qianli
# @file: addStrings.py
# @time: 2019/09/11
def addStrings(num1, num2):
    N1 = len(num1)
    N2 = len(num2)
    if N1 == '':
        return int(N2)
    if N2 == '':
        return int(N1)

    insert_d = '0' * abs(N1 - N2)
    a, b = num1[::-1], num2[::-1]
    if N1 < N2:
        a += insert_d
    else:
        b += insert_d
    res = 0
    data = ''
    for i in range(len(a)):
        value = (res + int(a[i]) + int(b[i])) % 10
        res = (res + int(a[i]) + int(b[i])) // 10
        data += str(value)
    if res == 1:
        data += str(res)
    return data[::-1]

num1 = '199'
num2 = '9'
print(int(num1)+int(num2))
print(addStrings(num1, num2))


