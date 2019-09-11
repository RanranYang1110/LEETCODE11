#-*- coding:utf-8 -*-
# @author: qianli
# @file: myAtoi.py
# @time: 2019/09/11
def myAtoi(str):
    '''将字符串转换成整数'''
    if len(str) == 0:
        return 0
    for j in range(len(str)):
        if str[j] != ' ':
            break
    str = str[j:]
    if len(str) == 0:
        return 0
    if str[0] not in ['-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+']:
        return 0
    if len(str) == 1 and str[0] in ['+', '-']:
        return 0
    elif len(str) == 1:
        return int(str[0])

    for i in range(1, len(str)):
        if str[i] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            break
    if i == len(str) - 1:
        i += 1
    str = str[:i]
    for mm in range(i+1):
        if str[mm] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            break
    str1 = str[mm:]
    if str[mm - 1] == '-':
        dd = int(str1) * -1
    elif str[mm - 1] == '+':
        dd = int(str1)
    else:
        dd = int(str1)

    if dd > 2 ** 31 - 1:
        return 2 ** 31 - 1
    if dd < - 2 ** 31:
        return - 2 ** 31
    return dd

def myAtoi2(str):
    if len(str) == 0:
        return 0
    str1 = str.replace(' ','')
    str1 = str1.replace('+', '')
    str1 = str1.replace('-', '')
    if len(str1) == 0:
        return 0
    if str1[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return 0
    for j in range(len(str)):
        if str[j] != ' ':
            break
    str = str[j:]
    res = 1
    if str[0] in ['+','-'] and str[1] in ['+', '-']:
        return 0
    elif str[0] in ['+', '-'] and str[1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return 0
    elif str[0] in ['+','-']:
        for jj in range(len(str)):
            if str[jj] not in ['+', '-']:
                break
        if jj == len(str):
            return 0
        str2 = str[jj:]
        b = str[jj-1]
        res = 1 if b == '+' else -1
    else:
        str2 =str
    for ii in range(len(str2)):
        if str2[ii] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            break
    if str2[ii] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        res_data = int(str2[:ii + 1]) * res
    else:
        res_data =  int(str2[:ii]) * res
    if res_data > 2 ** 31 - 1:
        return 2 ** 31 - 1
    if res_data < - 2 ** 31:
        return - 2 ** 31
    return res_data
strmm = '+-1'
print(myAtoi2(strmm))
# strmm = '45z'
strmm = '-91283472332'
strmm = ''
print(myAtoi2(strmm))
strmm = '1'
print(myAtoi2(strmm))

strmm = 'az1'
print(myAtoi2(strmm))

strmm = '43'
print(myAtoi2(strmm))

strmm = '- 234a'
print(myAtoi2(strmm))

