#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_if_else.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 20:12    Qihao      1.0         None
'''
# import lib
'''
if-else语句格式：
if 判断条件:
    条件成立时要执行的语句
    ...
else:
    条件不成立时要执行的语句
    ...
'''

# 以输入年龄判定是否可以去网吧上网为例
age = int(input("请输入您的年龄："))
if (age >= 18) :
    print(f"您输入的年龄是{age}岁，年满18周岁，可以到网吧上网.")
else:
    print(f"您输入的年龄是{age}岁，未满18周岁，不能到网吧上网.小盆友，请回家写作业去.")
