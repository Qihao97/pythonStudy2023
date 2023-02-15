#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_06_defaultParameter.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/14 22:32    Qihao      1.0         None
'''
# import lib

"""
缺省参数，也叫默认参数，在定义函数的时候，为参数提供默认值，调用函数的时候，可以不传该参数的值
注意：在函数的定义和调用的时候，所有的位置参数必须在默认参数之前
"""

# 示例默认参数：
def stu_info(name, age, gender = "female"):
    print(f"该学生姓名为：{name}， 年龄为：{age}， 性别为：{gender}。")

stu_info("Jane", 18)
stu_info("Tom", 20, "male")

