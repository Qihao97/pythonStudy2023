#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_05_dictionary_lookup.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/21 19:46    Qihao      1.0         None
'''
# import lib

"""
字典常用操作之查找
1. 按key值查找
    用法：字典序列名[key]
    如果当前查找的key存在，返回对应的value值，否则报错
2. get()函数
    用法： 字典序列.get(key, 默认值)
    如果查找的key值不存在，则返回默认值，缺省的默认值为None
3. keys()
    用法： 字典序列.keys()
    查找该字典序列所有的key值，返回可迭代对象
4. values()
    用法： 字典序列.values()
    查找该字典序列所有的value值，返回可迭代对象
5. items()
    用法： 字典序列.items()
    查找该字典序列所有的键值对，返回可迭代对象，里面的每个键值对以元组的形式出现
    每个元组的第一个数据是键值对的key值，第二个数据是键值对的value值
"""

# 按key值查找
dict1 = {"name" : "Jane", "age" : 18, "gender" : "female"}
print(dict1["name"])

# get()函数
print(dict1.get("name", "Null"))
print(dict1.get("nam", "Null"))

# keys()函数
print(dict1.keys())

# values()函数
print(dict1.values())

# items()函数
print(dict1.items())