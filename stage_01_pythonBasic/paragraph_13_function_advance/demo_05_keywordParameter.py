#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_05_keywordParameter.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/14 22:10    Qihao      1.0         None
'''
# import lib

""""
关键字参数：函数调用的时候，通过“键=值”的形式进行调用，可以使函数调用更加清晰，
更容易使用，同时也清除了函数参数的顺序要求
注意： 在函数调用时，如果有位置参数时，位置参数必须在关键字参数之前，而关键字参数之间不存在先后顺序
"""

def stu_info(name, age, gender):
    print(f"该学生的名字为：{name}， 年龄为：{age}， 性别为：{gender}。")

# 使用关键字参数调用以上函数
stu_info(age = 18, gender = "female", name = "Jane")


