#-*- coding:utf-8 -*-
# @author: qianli
# @file: test_deque.py
# @time: 2019/10/30
from collections import deque
q = deque()
q.append('eat')
q.append('sleep')
q.append('code')

#删除
q.popleft()

q.popleft()

q.popleft()