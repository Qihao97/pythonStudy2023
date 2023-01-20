#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_dictionary_modify.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/20 23:37    Qihao      1.0         None
'''
# import lib

"""
修改字典序列：
语法： 字典序列[key] = value
如果key存在则修改key对应的值，如果key不存在则新增此键值对
"""

dict1 = {"name" : "Jane", "age" : 18, "gender" : "female"}
print(dict1)
dict1["name"] = "Lily"
print(dict1)
dict1["num"] = "1001"
print(dict1)
