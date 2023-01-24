#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_operator.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/24 21:47    Qihao      1.0         None
'''
# import lib

"""
1. + 运算符：合并，支持字符串、列表、元组，不支持字典
2. * 运算符：复制，支持字符串、列表、元组，不支持字典
"""

# 1. + ：合并
s1 = "hello "
s2 = "world"
s3 = s1 + s2

list1 = ["hello ", "world"]
list2 = ["love ", "python"]
list3 = list1 + list2

tuple1 = ("hello ", "world")
tuple2 = ("love ", "python")
tuple3 = tuple1 + tuple2

dict1 = {"name" : "Jane", "age" : 18}
dict2 = {"gender" : "female"}

print(s3)
print(list3)
print(tuple3)

print("---------------****************-----------------")

# * : 复制
s1 = "hello world\t"
print(s1 * 5) # 输出5个s1

list4 = list1 * 2 + list2 * 2
print(list4)

tuple4 = tuple1 * 2 + tuple2 * 2
print(tuple4)

