#-*- coding:utf-8 -*-
# @author: qianli
# @file: rotateRight.py
# @time: 2019/09/16
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

def list_2_linknode(array):
    tem_node = ListNode()
    node = ListNode()
    for i in array:
        #记得是判定val是否有值，并且用一个node记住头节点，然后返回的是头节点          
        if not tem_node.val:
            tem_node.val = i
            node = tem_node
        else:
            tem_node.next = ListNode(i)
            tem_node = tem_node.next
    return node

def rotateRight(head, k):
    if not head: return None
    if not head.next: return head
    tail, cut, length = head, head, 0
    while tail.next:
        tail = tail.next
        length += 1
    k = k % (length + 1)
    for i in range(length - k): cut = cut.next
    tail.next = head
    res, cut.next = cut.next, None
    return res

data = [1,2,3,4,5]
mm = list_2_linknode(data)
# sl = LinkList()
# mm = sl.initlist_tail(data)

# print(sl.initlist_tail(data))
# print(rotateRight(mm, 5))
