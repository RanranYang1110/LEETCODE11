#-*- coding:utf-8 -*-
# @author: qianli
# @file: countAndSay.py
# @time: 2019/08/12
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        count_num = 0
        num = ''
        strs = ''
        for char in self.countAndSay(n-1):
            if char != num:
                if count_num > 0:
                    strs += str(count_num) + num
                count_num = 1
                num = char
            else:
                count_num += 1
        strs += str(count_num) + char
        return strs
clf = Solution()
print(clf.countAndSay(30))