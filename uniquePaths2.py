#-*- coding:utf-8 -*-
# @author: qianli
# @file: uniquePaths2.py
# @time: 2019/09/16
#-*- coding:utf-8 -*-
# @author: qianli
# @file: uniquePaths.py
# @time: 2019/09/16
def uniquePaths(m,n):
    '''一个机器人位于一个m*n网格的左上角，机器人每次只能向下或向右
    移动一步，问总共有多少条不同的路径？'''
    if m == 1 or n == 1:
        return 1
    cur = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            cur[j] += cur[j-1]
    return cur[-1]

print(uniquePaths(10, 3))
