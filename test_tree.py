#-*- coding:utf-8 -*-
# @author: qianli
# @file: test_tree.py
# @time: 2019/09/16
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def preTraverse(root):
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)

root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
print('前序遍历：')
preTraverse(root)

