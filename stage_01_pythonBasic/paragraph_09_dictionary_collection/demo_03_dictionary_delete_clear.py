#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_dictionary_delete_clear.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/19 23:19    Qihao      1.0         None
'''
# import lib

"""
字典的删除操作，del函数和clear方法
del()：删除字典或者删除字典中指定键值对

clear(): 清空字典
"""

dict1 = {"name" : "Jane", "age" : 18, "gender" : "male"}
print(dict1)
# 只删除一个键值对
del dict1['gender']
print(dict1)
# del函数删除字典
# del dict1
# 会报错
# print(dict1)

# clear()函数，清空字典
dict1.clear()
print(dict1)


