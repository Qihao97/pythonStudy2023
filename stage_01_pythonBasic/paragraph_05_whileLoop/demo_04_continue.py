#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_continue.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 15:44    Qihao      1.0         None
'''
# import lib
"""
continuw语句： 当条件成立的时候，退出当前一次循环，继而执行下一次循环
例如： 吃苹果案例，当吃到第三个苹果的时候，吃到一只虫子，这个苹果就不吃了，吃下一个
"""
i = 1
while (i <= 5):
    # 吃到第三个苹果的时候，吃到虫子了，停掉，吃下一个
    if (i == 3):
        print("吃到一个大虫子，这个苹果不吃了.")
        i += 1
        continue
    print(f"吃了第{i}个苹果.")
    i += 1


