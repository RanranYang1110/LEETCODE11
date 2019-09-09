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

def isPalindrome(s):
    return "".join(filter(str.isalnum, s)).lower()[::-1] == "".join(filter(str.isalnum, s)).lower()[::-1]
    #%%
s = 'A man, a plan, a a canal : Panama'
# for i in [' ', ',', ':', '.']:
#     s = s.replace(i, '')
# s = s.lower()
print(isPalindrome(s))


