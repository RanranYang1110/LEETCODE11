#-*- coding:utf-8 -*-
# @author: qianli
# @file: simplifyPaht.py
# @time: 2019/11/01
def simplifyPath(path):
    '''
    :简化路径
    :param path: 输入路径
    :return: 简化后的路径
    '''
    lst = []
    splits = path.split('/')
    for s in splits:
        if s == '':
            continue
        if s == '.':
            continue
        if s == '..':
            if len(lst) != 0:
                lst.pop()
        else:
            lst.append(s)
    result = []
    result = ['/' + i for i in lst]
    return ''.join(result)
path = "/home/"
print(simplifyPath(path))
path = "/a/./b/../../c/d/../e/f/g/../"
print(simplifyPath(path))
