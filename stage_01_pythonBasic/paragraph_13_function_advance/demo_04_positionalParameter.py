#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_positionalParameter.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/13 20:50    Qihao      1.0         None
'''
# import lib

"""
Python中的位置参数，python中的参数有：位置参数、关键字参数、默认参数（缺省参数）、不定长参数（可变参数）
parameter 为函数定义时的叫法, 它指明了函数可以接受的argument类型. 可以理解为C语言中的形参;
argument 为函数调用时的叫法, 可以理解为实参, 即传入的值;

位置参数：调用函数时根据函数定义的参数位置来传递参数，传递的参数和定义的参数的位置和数量必须保持一致，否则报错
"""

def stu_info(name, age, gender):
    """
    用来输出学生的姓名、年龄、性别
    :param name: string类型，学生姓名
    :param age: int类型，学生年龄
    :param gender: string类型，学生性别
    :return: null
    """
    print(f"学生的姓名为：{name}，年龄为：{age}，性别为：{gender}")

stu_info("Lily", 18, "female")
stu_info("Tom", 20, "male")


