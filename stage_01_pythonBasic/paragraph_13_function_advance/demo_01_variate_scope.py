#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_variate_scope.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/8 23:21    Qihao      1.0         None
'''
# import lib
"""
变量作用域：变量作用域指的是变量生效的范围：主要包括局部变量和全局变量
局部变量：定义在函数体内部的变量，只在函数体内部生效
作用：在函数体内部，临时保存数据，当函数调用完毕后，局部变量即销毁
特点：只能在指定的函数体内部访问，函数体外部不可访问

全局变量：定义在所有函数体外的变量，在函数体内外皆可访问，当程序运行结束后才销毁
"""

# 全局变量
a = 100

def testA():
    print(a)

def testB():
    print(a)

testA()
testB()
print(a)

"""
修改全局变量：
1.如果直接在函数体内部用 a = 100 的方式来修改，是定义了同名局部变量，不影响全局变量
2.如果需要在函数体内部修改全局变量，要使用 global a 的方式先声明全局变量，然后再修改
"""
print("-"*27)
print("修改全局变量")

global_v = 100

def print_A():
    print(global_v)

def print_B():
    global_v = 300
    print(global_v)

def print_C():
    global global_v
    global_v = 500

print(global_v)
print("-------")
print_A()
print(global_v)
print("-------")
print_B()
print(global_v)
print("-------")
print_C()
print(global_v)




