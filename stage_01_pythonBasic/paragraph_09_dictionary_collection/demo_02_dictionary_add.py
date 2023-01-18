#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_dictionary_add.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/18 22:45    Qihao      1.0         None
'''
# import lib

"""
字典的常见操作，新增数据
语法：字典序列[key] = value

"""

# 测试字典新增数据
dict1 = {"name" : "Jane", "age" : 18, "num" : "1001"}
print(dict1)
dict1["gender"] = "female"
print(dict1)

