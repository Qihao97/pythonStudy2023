#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_multi_for.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/30 22:30    Qihao      1.0         None
'''
# import lib

"""
在列表推导式里写多个for循环
"""
# for循环嵌套实现列表：[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list1 = []
for i in range(1, 3):
    for j in range(3):
        list1.append((i, j))
print(list1)

# 列表推导式多个for循环实现列表：[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 相当于for循环的嵌套
list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)

