#-*- coding:utf-8 -*-
# @author: qianli
# @file: lastStoneWeight.py
# @time: 2019/08/08
def lastStoneWeight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    if len(stones) == 1:
        return stones[0]
    else:
        bb = sorted(stones, reverse=1)
        while len(bb) > 2:
            bb = sorted([bb[0] - bb[1]] + bb[2:], reverse=1)
        bb = sorted(bb, reverse=1)
        return bb[0] - bb[1]

stones = [2, 7, 4, 1, 8, 1]

print(lastStoneWeight(stones))