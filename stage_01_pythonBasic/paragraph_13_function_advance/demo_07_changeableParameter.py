#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_07_changeableParameter.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/16 22:04    Qihao      1.0         None
'''
# import lib

"""
不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数的场景。
此时，可以使用包裹（packing）位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。
"""

# 包裹位置参数
def stu_info(*args):
    print(args)
"""
注意：传进的所有参数都被args变量收集，它会根据传进参数的位置合并为一个元组（tuple），
args是元组类型，此为包裹位置传递，也可以是零个参数
"""

# 调用
# ('Tom',)
stu_info("Tom")
# ('Jane', 18)
stu_info("Jane", 18)

"""
不定长参数之关键字参数
"""

def stu_info1(**kwargs):
    print(kwargs)

# 调用该函数，kwargs参数会收集所有关键字参数，返回一个字典
# {'name': 'Tom', 'age': 18, 'gender': 'male'}
stu_info1(name = "Tom", age = 18, gender = "male")
