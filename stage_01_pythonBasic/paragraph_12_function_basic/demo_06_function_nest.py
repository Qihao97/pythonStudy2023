#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_06_function_nest.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/7 22:12    Qihao      1.0         None
'''
# import lib

"""
函数的嵌套调用：
所谓函数的嵌套调用，就是在一个函数里面又调用了另一个函数。
"""

def testB():
    print("-----  testB start  -----")
    print("-----  testB 执行中。。。  ---")
    print("-----  testB end  -----")

def testA():
    print("-----  testA start  -----")
    print("-----  调用testB  -----")
    testB()
    print("-----  testA end  -----")

testA()

print("-------------函数嵌套调用的应用，打印多条横线--------------")
# 应用：打印多条横线
# 打印一条横线
def print_line():
    print("-" * 20)

# 打印多条横线
def print_lines(n):
    for i in range(n):
        print_line()

print_lines(6)

