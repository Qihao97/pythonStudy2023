#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_07_list_nest.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/15 14:03    Qihao      1.0         None
'''
# import lib

"""
列表嵌套
1. 列表嵌套指的是一个列表里包含了其他的子列表
"""

# 测试列表的嵌套
name_list = [["Tom", "Jane", "Richard"], ["小明", "小红", "小强"], ["张三", "李四", "王五"]]
print(name_list)

# 列表嵌套到时候，如果取数据，即如何用下标取数据
print(f"name_list[0] = {name_list[0]}")
print(f"name_list[0][1] = {name_list[0][1]}")


