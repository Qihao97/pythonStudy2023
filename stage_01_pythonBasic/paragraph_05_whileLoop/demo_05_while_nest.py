#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_05_while_nest.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 16:06    Qihao      1.0         None
'''
# import lib

"""
while循环嵌套：
语法：
while (条件1):
    条件1成立时要执行的语句
    ...
    while (条件2):
        条件2成立时要执行的语句
        ...
"""
# while嵌套，四年的春夏秋冬
i = 1
j = 0
while (i <= 4):
    print(f"第{i}年.")
    i += 1
    while (j < 4):
        if (j == 0):
            print("春季")
        elif (j == 1):
            print("夏季")
        elif (j == 2):
            print("秋季")
        else:
            print("冬季")
        j += 1
    j = 0

# 打印星号正方形矩阵
"""
需求： 5 * 5 的*矩阵
"""
print("输出5*5 的星号矩阵")
i = 0
j = 0
while (i < 5):
    while (j < 5):
        print("*", end=' ')
        j += 1
    # 输出5个*之后换行
    print()
    # 将内层计数器j置0
    j = 0
    # 外层计数器i加1
    i += 1

"""
使用嵌套循环打印三角形星号
"""
print("使用嵌套循环打印三角形的星号")
j = 0
while (j < 5):
    i = 0
    # i表示每行里面星星的个数，这个数字要和行号相等，因此i和j要联动
    while (i <= j):
        print("*", end=" ")
        i += 1
    print()
    j += 1

'''
while循环输出九九乘法表
步骤：
1. 输出乘法表达式， x * x = n
2. 一行打印多个，个数等于行号，输出一行后换行
3. 打印多行
'''
print("使用while循环输出九九乘法表")
i = 1
while (i <= 9):
    j = 1
    while (j <= i):
        result = i * j
        print(f"{j} * {i} = {result}", end='\t')
        j += 1
    print()
    i += 1
