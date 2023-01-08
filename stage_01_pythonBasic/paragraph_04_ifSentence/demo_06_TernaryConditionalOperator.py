#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_06_TernaryConditionalOperator.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 0:09    Qihao      1.0         None
'''
# import lib
"""
三目运算符：
格式： 条件成立时执行的表达式 if 判断条件 else 条件不成立时执行的表达式
"""

a = 1
b = 2
c = a if (a > b) else b
print(c)