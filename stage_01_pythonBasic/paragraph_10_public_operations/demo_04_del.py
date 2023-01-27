#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_del.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/27 23:01    Qihao      1.0         None
'''
# import lib

"""
del或者del()： 删除

"""

# del 目标 或者 del(目标)

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

del s1
print(s1)

del tuple1
print(tuple1)
