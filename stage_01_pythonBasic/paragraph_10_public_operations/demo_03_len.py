#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_len.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/26 23:26    Qihao      1.0         None
'''
# import lib

"""
1. len方法用来计算容器中数据的个数
支持字符串、列表、元组、集合、字典
"""

s1 = "abcdefg"
print(len(s1))

list1 = ["hello", "world"]
print(len(list1))

tuple1 = ("a", "b", "c")
print(len(tuple1))

set1 = {"abc", "def", "g", "h", "i"}
print(len(set1))

dict1 = {"name" : "Jane", "age" : 18, "gender" : "female"}
print(len(dict1))
