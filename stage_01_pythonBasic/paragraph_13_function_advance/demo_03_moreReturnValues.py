#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_moreReturnValues.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/12 22:18    Qihao      1.0         None
'''
# import lib

"""
一个函数，多个返回值
1. 直接写 return 1, 2 默认返回的是元组
2. return后面可以写 元组、列表、字典等序列，以返回多个值
"""
# 示例：一个函数，返回两个值
def two_num():
    return 1, 2

# 输出 (1, 2)
print(two_num())



