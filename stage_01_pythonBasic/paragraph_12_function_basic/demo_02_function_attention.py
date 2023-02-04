#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_function_attention.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/4 22:32    Qihao      1.0         None
'''
# import lib

"""
函数的注意事项：
1. 先定义后使用
2. 只定义不调用的话，不执行
3. 调用函数的时候，程序转向定义函数的函数体处执行，执行完毕后，向下执行
"""

def show():
    print("Hello World!")

show()
