#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_whileGrammar.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 11:15    Qihao      1.0         None
'''
# import lib

"""
while循环的语法：
while 条件:
    条件成立时要执行的语句
    ...

"""
# while循环测试
i = 0
while (i < 100):
    print("Hello World!")
    i += 1
"""
计数器的习惯写法:
初始值一般写0，一般不加=号，需要执行N次就写 i < N
"""

