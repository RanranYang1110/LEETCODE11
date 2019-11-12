#-*- coding:utf-8 -*-
# @author: qianli
# @file: RandomizedSet.py
# @time: 2019/11/12
class RandomizedSet:
    '''常数时间插入、删除和获取随机元素'''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.index = 0
        self.len = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False
        else:
            self.data[val] = self.index
            self.index += 1
            self.len += 1
            return True
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data:
            return False
        else:
            del self.data[val]
            self.len -= 1
            return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        if self.len == 0:
            return False
        else:
            return random.choice(list(self.data.keys()))