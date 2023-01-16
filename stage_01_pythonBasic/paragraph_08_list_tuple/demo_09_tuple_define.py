#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_09_tuple_define.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/16 22:55    Qihao      1.0         None
'''
# import lib

"""
1. 一个元组可以存储多个数据，元组内的数据不可修改，而列表中的数据是允许修改的
2. 列表中的元素用方括号[]括起来，元组中的数据用圆括号()括起来
3. 定义元组使用圆括号，元组中的各个数据用英文逗号隔开，数据可以是不同类型
4. 注意：如果定义的元组只有一个数据，那么这个数据后面也要加逗号，否则数据类型为此数据的类型，不判定为元组

"""

# 体验单个数据和多个数据的不同：
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1,)
tuple3 = (1)
tuple4 = ("aaa")
tuple5 = ("aaa",)

print(tuple1)
print(type(tuple1))
print(tuple2)
print(type(tuple2))
print(tuple3)
print(type(tuple3))
print(tuple4)
print(type(tuple4))
print(tuple5)
print(type(tuple5))

