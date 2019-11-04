#-*- coding:utf-8 -*-
# @author: qianli
# @file: hasCycle.py
# @time: 2019/09/27
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
def find_beginning(head):
    '''给定一个链表，返回链表开始入环的第一个节点。'''
    if head is None:
        return None
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            break
    if fast is None or fast.next is None:
        return None
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return slow


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = node1
print(find_beginning(node1).value)
node3.next = node2
print(find_beginning(node1).value)