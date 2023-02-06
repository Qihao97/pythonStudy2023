#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_05_function_doc.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/6 22:02    Qihao      1.0         None
'''
# import lib

"""
定义函数的说明文档

"""

"""
help(函数名) 可以用于说明函数的作用
help(len)
输出：
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
"""
help(len)

# 函数的说明文档，函数的文档说明
"""
def 函数名(参数列表):
    ""/" 说明文档位置  ""/"
    函数体
    return 
"""

def my_sum(a, b):
    """求和函数"""
    return a + b

print("-" * 18)
help(my_sum)

def my_add(a, b, c):
    """
    三个数求和
    :param a: 整数
    :param b: 整数
    :param c: 整数
    :return: 整数
    """
    return a + b + c

print("*" * 18)
help(my_add)

