#-*- coding:utf-8 -*-
# @author: qianli
# @file: kthSmallest.py
# @time: 2019/09/16
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthSmallest(root, k):
    '''给定一个二叉搜索树，查找其中第k个最小的元素'''
    cur = root
    stack = []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        tmp = stack.pop()
        k -= 1
        if k == 0:
            return tmp.val
        if tmp.right:
            cur = tmp.right
global null
null = ''
root = [3,1,4,null,2]
mm = TreeNode(root)
k = 1
print(kthSmallest(mm, k))

