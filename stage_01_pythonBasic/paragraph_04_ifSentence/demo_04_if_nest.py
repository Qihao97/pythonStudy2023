#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_if_nest.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 23:21    Qihao      1.0         None
'''
# import lib

'''
if语句的嵌套
语法
if 条件1:
    条件1成立时要执行的代码
    ...
    if 条件2: # 条件2的if语句处于条件1成立时的执行代码缩进内
        条件2成立时要执行的代码
        ...
'''
"""
需求：坐公交，有钱，钱够了才可以上车，没有钱就没法上车
上车之后，如果有空位，就可以坐下，否则就无法坐下
步骤：
1.准备用来判断的数据， 钱和空座
2.判断是否有钱，输出是否可以上车
3.判断是否可以入座：有无空座
"""

money = 1
seat = 1

if money >= 1:
    print("土豪，请上车.")
    if seat >= 1:
        print("有座位，请入座.")
    else:
        print("没有座位了，只能站着了.")
else:
    print("朋友，没带钱，跟着跑，跑快点.")
