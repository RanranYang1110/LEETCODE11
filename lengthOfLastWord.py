#-*- coding:utf-8 -*-
# @author: qianli
# @file: lengthOfLastWord.py
# @time: 2019/08/12
def lengthOfLastWord(self, s: str) -> int:
    strs = s.split(' ')
    if len(strs) == 0:
        return 0
    else:
        mm = []
        for ii in range(len(strs)):
            if strs[ii] != '':
                mm.append(strs[ii])
        if len(mm) == 0:
            return 0
        else:
            return len(mm[-1])
    return len(strs[-1])