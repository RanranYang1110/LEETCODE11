#-*- coding:utf-8 -*-
# @author: qianli
# @file: merge2.py
# @time: 2019/09/19
def merge(intervals):
    '''给出一个区间的集和，合并所有重叠的区间'''
    # intervals.sort(key=lambda x: x.start)
    intervals = sorted(intervals)
    if len(intervals) < 2:
        return intervals
    for i in range(1, len(intervals)):
        if intervals[i][0] <= intervals[i-1][1]:
            intervals[i][0] = intervals[i-1][0]
            if intervals[i][1] < intervals[i-1][1]:
                intervals[i][1] = intervals[i-1][1]
            intervals[i-1] = []
    while [] in intervals:
        intervals.remove([])
    return intervals
intervals = [[1, 3],[2, 6],[8, 10],[15, 18]]
# intervals = [[1, 4], [0, 2], [3,5]]
print(merge(intervals))