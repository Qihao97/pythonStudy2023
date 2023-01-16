#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_10_tuple_methods.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/16 23:07    Qihao      1.0         None
'''
# import lib

"""
元组中的数据不支持修改，其查找操作有：
1. 按下标查找： tuple[i]
2. index(): 语法为：tuple1.index("aa") 
    在元组中查找某一个元素，如果存在，返回对应的下标，否则报错
3. count():  tuple1.count("aa")
    统计某个数据在当前元组中出现的次数
4. len(): len(tuple1)
    统计元组中数据的个数
    
元组内的直接数据不支持修改，如果修改，立即报错，但是如果元素为列表，则可修改列表
"""

# 按下标取数据
tuple1 = ("hello", "world", "python", "heima", "python")
print(tuple1[0])

# index()方法
i = tuple1.index("python")
print(f"hello 的下标为： {i}")

# count()方法
c = tuple1.count("python")
print(f"python 出现的次数为： {c}")

# len()方法
l = len(tuple1)
print(f"元组tuple1的长度为： {l}")

tuple2 = ("a", "b", "c", ["d", "e"])
# 直接修改，报错
# tuple2[0] = "f"
print(tuple2)
tuple2[3][1] = "Jane"
print(tuple2)
