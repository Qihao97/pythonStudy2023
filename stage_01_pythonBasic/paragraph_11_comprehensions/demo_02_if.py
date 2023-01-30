#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_if.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/30 22:23    Qihao      1.0         None
'''
# import lib

"""
带if语句的列表推导式
"""
# 创建0到10的偶数序列

# 步长实现
list1 = [i for i in range(0, 10, 2)]
print(list1)

# for循环加if实现
list2 = []
for i in range(10):
    if(i % 2 == 0):
        list2.append(i)
print(list2)

# 列表推导式加if实现
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)

