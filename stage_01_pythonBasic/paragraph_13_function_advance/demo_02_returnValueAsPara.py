#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_returnValueAsPara.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/11 23:49    Qihao      1.0         None
'''
# import lib

"""
函数返回值作为参数传递
"""

def testA():
    return 100

def testB(a):
    print(a)

testB(testA())

