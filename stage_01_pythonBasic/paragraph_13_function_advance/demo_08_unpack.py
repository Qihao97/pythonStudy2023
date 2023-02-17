#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_08_unpack.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/17 21:51    Qihao      1.0         None
'''
# import lib

"""
元组和字典的拆包操作
"""
# 元组的拆包示例
def return_nums():
    return 100, 200

nums = return_nums()
print(nums)

print("*" * 21)

result1, result2 = return_nums()
print(result1)
print(result2)

print("*" * 21)

# 字典的拆包示例
dict1 = {"name" : "Jane", "age" : 18}
a, b = dict1

# 对字典进行拆包，取出来的是字典的key
print(a)
print(b)

print("*" * 21)

print(dict1[a])
print(dict1[b])
