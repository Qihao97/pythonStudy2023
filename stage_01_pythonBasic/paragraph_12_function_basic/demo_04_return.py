#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_return.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/5 22:20    Qihao      1.0         None
'''
# import lib

"""
如果需要函数返回内容给调用者，可以使用return语句进行返回
return语句的特点：
    1. 负责函数返回值
    2. 退出当前函数，在函数体中，执行到return语句就不再往下执行了
"""
# 带返回值的函数，返回 烟
def buy():
    return '烟'

goods = buy()
print(goods)


