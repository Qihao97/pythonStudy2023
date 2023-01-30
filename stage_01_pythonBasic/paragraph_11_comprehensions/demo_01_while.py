#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_while.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/30 20:54    Qihao      1.0         None
'''
# import lib

"""
使用while循环创建有规律的列表
"""

# 使用while循环实现一个0，1，2，3...的列表
i = 0
list1 = []
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# for循环实现
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 使用列表推导式实现
list3 = [i for i in range(10)]
print(list3)
