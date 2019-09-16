#-*- coding:utf-8 -*-
# @author: qianli
# @file: generateMatrix.py
# @time: 2019/09/16
def generateMatrix(n):
    '''
    给定一个正整数n，生成一个包含1到n2所有元素，
    且元素按顺时针顺序螺旋排列的正方形矩阵
    '''
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    seen = [[False] * n for _ in matrix]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0
    num, target = 1, n * n
    while num <= target:
        matrix[r][c] = num
        num += 1
        seen[r][c] = True
        cr, cc = r + dr[di], c + dc[di]
        if 0 <= cr < n and 0 <= cc < n and seen[cr][cc] == False:
            r = cr
            c = cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    return matrix

print(generateMatrix(3))