#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_dictionary_garmmar.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/17 23:09    Qihao      1.0         None
'''
# import lib

"""
字典里的数据以键值对的形式存在，字典里的数据和其顺序没有关系，即字典不支持下标，
后期无论数据顺序如何变化，只需要按照键名查找数据即可
创建字典：
1. 字典用花括号括起来
2. 数据以键值对形式存在
3. 各数据之间用逗号隔开
"""

# 有数据的字典：
dict1 = {"name" : "Jane", "age" : 18, "gender" : "female"}
print(type(dict1))
print(dict1)

# 无数据的字典：
dict2 = {}
print(dict2)

# 使用dict()函数来创建空字典
dict3 = dict()
print(dict3)

