#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_if.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 19:15    Qihao      1.0         None
'''
# import lib
'''
if语句的基本语法：
if 判断条件:
    条件成立时要执行的语句
    ...
'''
# eg: 如果年满18周岁，就可以到网吧上网
age = 20

if (age >= 18) :
    print("年满18周岁，可以到网吧上网.")

# 用户输入一个年龄，然后根据输入的年龄进行判断是否可以上网
print("用户输入一个年龄，然后根据输入的年龄进行判断是否可以上网")
age = eval(input("请输入您的年龄："))
if (age >= 18) :
    print(f"您输入的年龄是{age}岁，年满18周岁，可以到网吧上网.")
