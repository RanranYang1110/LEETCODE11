#-*- coding:utf-8 -*-
# @author: qianli
# @file: findRestaurant.py
# @time: 2019/09/18
def findRestaurant(list1, list2):
    map1 = {list1[i]:i for i in range(len(list1))}
    map2 = {list2[i]:i for i in range(len(list2))}
    inter = list(set(list1) & set(list2))
    res = []
    data_in = {i: map1[i] + map2[i] for i in inter}
    res = []
    # for i in inter:
    #     if data_in[i] == min(data_in.values()):
    #         res.append(i)
    # return res
    return [val for val in inter if data_in[val] == min(data_in.values())]
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findRestaurant(list1, list2))