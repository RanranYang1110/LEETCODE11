#-*- coding:utf-8 -*-
# @author: qianli
# @file: searchMatrix.py
# @time: 2019/09/23
def searchMatrix(matrix, target):
    '''时间复杂度O(log（mn）)'''
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    # 二分查找
    left, right = 0, m * n - 1
    while left <= right:
        pivot_idx = (left + right) // 2
        pivot_element = matrix[pivot_idx // n][pivot_idx % n]
        if target == pivot_element:
            return True
        else:
            if target < pivot_element:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1
    return False

def searchMatrix2(matrix, target):
    '''时间复杂度: O(m+n)'''
    if len(matrix) == 0:
        return False
    height, width = len(matrix), len(matrix[0])
    row, col = height-1, 0
    while row>=0 and col < width:
        start = matrix[row][col]
        if start < target: col += 1
        elif start > target: row -= 1
        else: return True

def searchMatrix3(matrix, target):
    if len(matrix) == 0:
        return False
    height, width = len(matrix), len(matrix[0])
    row, col = height-1, 0
    while row >= 0 and col < width:
        if matrix[row][col] > target: row -= 1
        elif matrix[row][col] < target: col += 1
        else: return True
    return False

matrix = [[1,3,5,7],[10, 11, 16, 20],[23, 30, 34, 50]]
print(searchMatrix3(matrix, 5))