#-*- coding:utf-8 -*-
# @author: qianli
# @file: longestPalindrome.py
# @time: 2019/09/12
def longestPalindrome(s):
    '''判断最长回文数'''
    size = len(s)
    if len(s) <= 1:
        return s
    dp = [[False for _ in range(size)] for _ in range(size)]

    longest_1 = 1
    res = s[0]
    for r in range(1, size):
        for l in range(r):
            if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                dp[l][r] = True
                cur_len = r - l + 1
                if cur_len > longest_1:
                    longest_1 = cur_len
                    res = s[l : r+1]
    return res
s = 'abab'
s1 = s[::-1]
print(longestPalindrome(s))