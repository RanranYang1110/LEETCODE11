#-*- coding:utf-8 -*-
# @author: qianli
# @file: test.py
# @time: 2019/08/24
global null
null = None
# mm = {'a':null, 'b':1}
import pandas as pd
import numpy as np
# data = pd.DataFrame(mm)

# import json
# aa = '{"a":null, "b":1}'
# aa = json.loads(aa)
aa = np.array([[1,2,3],[4,5,null]])

data = pd.DataFrame(aa)
data[data.isnull()] = 20