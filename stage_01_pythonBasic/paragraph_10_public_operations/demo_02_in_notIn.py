#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_in_notIn.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/25 21:47    Qihao      1.0         None
'''
# import lib

"""
in 和 not in 操作符用来判断某个数据在不在序列中
支持字符串、列表、元组、字典
返回结果为True或者False
"""

s1 = "helloworld!"
list1 = ["hello", "world"]
tuple1 = ("hello", "world")
dict1 = {"name" : "Jane", "age" : 18, "gender" : "female"}

print("hello" in s1)
print("hello" in list1)
print("hello" in tuple1)

# in, not in判断字典
print("in, not in判断字典")
print(("name", "Jane") in dict1.items())
print("name" in dict1)
print("Jane" in dict1)  # 输出False
print("name" in dict1.keys())
print("Jane" in dict1.values())
