#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_09_swapValueOfVariates.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/17 22:13    Qihao      1.0         None
'''
# import lib
"""
交换两个变量的值：
1.定义第三个变量作为中间变量
2. a, b = 1, 2
   a, b = b, a
"""

# 定义中间变量实现两个变量值的交换
a = 1
b = 2
# 定义中间变量c
c = a
a = b
b = c

print(a)
print(b)

print("*---" * 12)
# 简化代码
a1, b1 = 1, 2
a1, b1 = b1, a1
print(a1)
print(b1)

