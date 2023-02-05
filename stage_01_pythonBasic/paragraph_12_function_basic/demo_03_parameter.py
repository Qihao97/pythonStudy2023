#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_parameter.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/5 22:05    Qihao      1.0         None
'''
# import lib

"""
带参数的函数
"""

# 定义带参数的函数
def my_add(a, b):
    result = a + b
    print(result)

# 调用函数
my_add(1, 2)
my_add("Hello ", "World!")

