#-*- coding:utf-8 -*-
# @author: qianli
# @file: addTwoNumbers1.py
# @time: 2019/09/10
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr, carry = dummyHead, 0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(1)
        return dummyHead.next




