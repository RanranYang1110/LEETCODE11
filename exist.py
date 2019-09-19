#-*- coding:utf-8 -*-
# @author: qianli
# @file: exist.py
# @time: 2019/09/19
class Solution:
    def __init__(self):
        self.trans = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def exist(self, board, word):
        '''给定一个二维网格和一个单词，找出该单词是否存在于网格中'''
        pos = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        M, N = len(board), len(board[0])

        for i in range(M):
            for j in range(N):
                #对每个格子都从头到尾搜索
                if self.search_word(board, word, 0, i, j, pos, M, N):
                    return True
        return False
    def search_word(self, board, word, index, start_x, start_y, marker, m, n):
        # 递归终止条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]
        if board[start_x][start_y] == word[index]:
            marker[start_x][start_y] = True
            for direction in self.trans:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0<=new_x<m and 0<=new_y<n and not marker[new_x][new_y] and  \
                        self.search_word(board, word, index + 1, new_x, new_y, marker, m, n):
                    return True
            marker[start_x][start_y] = False
        return False


board = [['A','B','C','E'], ['S','F','C','S'],['A','D','E','E']]
word = 'ABCCED'
clf = Solution()
print(clf.exist(board, word))


