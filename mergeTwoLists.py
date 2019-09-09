#-*- coding:utf-8 -*-
# @author: qianli
# @file: mergeTwoLists.py
# @time: 2019/09/02
class ListNode:
    def __init_(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, L1, L2):
        if L1 is None:
            return L2
        elif L2 is None:
            return L1
        elif L1.val < L2.val:
            L1.next = self.mergeTwoLists(L1.next, L2)
            return L1
        else:
            L2.next = self.mergeTwoLists(L1, L2.next)
            return L2

L1 = [1,2,4]
L2 = [1,3,4]
clf = Solution()
print(clf.mergeTwoLists(L1, L2))

ListNode(L1)


class Lnode():
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_
class LinkedList():
    def __init__(self):
        self._head=Lnode(None)
    def is_empty(self):
        return self._head.next is None
    def prepend(self,elem):
        self._head.next=Lnode(elem,self._head.next)
    def append(self,elem):
        p=self._head
        while (p.next is not None):
            p=p.next
        p.next=Lnode(elem)
    def insert(self,elem,i):
        if i<0 or not isinstance(i,int):
            raise ValueError('Invalid index')
        else:
            index=0
            p=self._head
            while p is not None:
                if index==i:
                    p.next=Lnode(elem,p.next)
                    break
                else:
                    p=p.next
                    index+=1
    def pop(self):
        if self._head.next is None:
            raise ValueError('No element to pop')
        else:
            e=self._head.next.elem
            self._head.next=self._head.next.next
            return e
    def find(self,elem):
        p=self._head
        index=0
        while p is not None:
            if p.next.elem==elem:
                return index
            else:
                p=p.next
                index+=1
            return 'Not find'
    def __str__(self):
        p=self._head
        temp=''
        while p.next is not None:
            temp+=str(p.next.elem)
            temp+='->'
            p=p.next
            temp+='None'
            return temp
l1 = LinkedList()
mode = Lnode(1)
import numpy as np
np.random.normal(mu,sigma, n)