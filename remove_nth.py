#-*- coding:utf-8 -*-
# @author: qianli
# @file: remove_nth.py
# @time: 2019/09/27


class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
class Linklist:
    def __init__(self):
        self.head = Node()
        self.size = 0
    def add_first(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    def length(self):
        return self.size
    def add_last(self, value):
        new_node = Node(value)
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new_node
        self.size += 1
    def print_list(self):
        node = self.head
        while node.next != None:
            node = node.next
            print(node.value, end= ' ')
        print()
def remove_nth(lst, n):
    assert n<=lst.length and n >0
    fast = lst.head
    while n>0:
        fast = fast.next
        n -= 1
    slow = lst.head
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    result = slow.next
    slow.next = slow.next.next
    lst.length = lst.length - 1
    return result

ll = Linklist()
ll.add_first(6)
ll.add_first(8)
ll.add_last(10)
ll.add_last(14)
m = remove_nth(ll, 2)