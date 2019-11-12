#-*- coding:utf-8 -*-
# @author: qianli
# @file: isPalindrome.py
# @time: 2019/08/18
def isPalindrome(s):
    for i in [' ', ',', ':', '.']:
        s = s.replace(i, '')
    s = s.lower()
    if len(s) == 0:
        return True
    else:
        for ii in range(int(len(s)/2)):
            if s[ii] != s[len(s)-1-ii]:
                return False
        return True

def isPalindrome4(s):
    if len(s) == 0:
        return True
    s = s.lower()
    s1 = ''
    for str1 in s:
        if str1.isalnum():
            s1 += str1.lower()
    for ii in range(len(s1)):
        if s1[ii] != s1[len(s1)-1-ii]:
            return False
    return True

def isPalindrome1(s):
    return "".join(filter(str.isalnum, s)).lower()[::-1] == "".join(filter(str.isalnum, s)).lower()[::-1]

s = 'A man, a plan, a a canal : Panama'
# s = 'ab@a'
# for i in [' ', ',', ':', '.']:
#     s = s.replace(i, '')
# s = s.lower()
print(isPalindrome4(s))


