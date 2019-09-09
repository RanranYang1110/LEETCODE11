#-*- coding:utf-8 -*-
# @author: qianli
# @file: isValidSudoku.py
# @time: 2019/09/09
def isValidSudoku(board):
    '''判断是否是有效的数独'''
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3) * 3 + j // 3

                rows[i][num] = rows[i].get(num, 0) + 1
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False
    return True


x = [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(x))