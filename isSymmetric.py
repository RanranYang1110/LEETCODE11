#-*- coding:utf-8 -*-
# @author: qianli
# @file: isSymmetric.py
# @time: 2019/09/02
def isSymmetric(root):
    '''给定一个二叉树，检查它是否是镜像对称的'''
    def match(l, r):
        if not l and not r: return True
        if not l or not r: return False
        return l.val == r.val and match(l.left, r.right) and match(l.right, r.left)

    return match(root, root)
def mergeTrees(t1, t2)

     if t1 and t2:
         t1.val = t1.val + t2.val
         # left 繁衍
         t1.left = self.mergeTrees(t1.left, t2.left)
         # right 繁衍
         t1.right = self.mergeTrees(t1.right, t2.right)
     elif not t1 and t2:
         return t2
     else:
         return t1

     return t
