#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_operator.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 13:49    Qihao      1.0         None
'''
# import lib
'''
Python中运算符的分类：
1.算术运算符
    1.1 算术运算符包括+、-、*、/, // 整除，即只保留整数部分，% 取余或者叫取模，** 指数， () 圆括号，用来改变运算优先级
    1.2 混合运算优先级： ()高于 ** 高于 * / // % 高于 + -
2.赋值运算符
    2.1 赋值运算符 = ，作用是将 = 右边的表达式运算结果赋值给 = 左侧的变量
    2.2 python允许用一个 = 完成多个变量的赋值操作，但是=两边的变量和表达式要严格一一对应
    2.3 也可以使用 = 同时给多个变量赋同一个值， e.g. a = b = 100
3.复合赋值运算符
    3.1 复合赋值运算符包括 += -= *= /=  //=  %=  **=
    3.2 复合赋值运算符相当于运算后再赋值，例如 += 就相当于 运算符左右两边先执行加法运算，然后把运算结果赋值给左边
4.比较运算符
    4.1 比较运算符，用来判断两边的值是否满足相等，不等，大于小于等关系，返回的是布尔值，需要布尔变量接收
    4.2 比较运算符有: ==, !=, >, <, >=, <=
5.逻辑运算符
    5.1 逻辑运算符有： and：逻辑与，or：逻辑或，not：逻辑非
    5.2 这三个逻辑运算符用来连接两个表达式，返回布尔True或者False
    5.3 这个逻辑运算符的优先级如下： not > and > or, 在使用中，为避免歧义，尽量加圆括号()
    5.4 数字之间的逻辑运算：
        （1）and运算符，只要参与运算的数字有一个为0，则运算结果为0，否则是参与运算的最后一个数字
        （2）or运算符，只有所有参与运算的数字都为0时，运算结果才是0，否则为参与运算的第一个非0数字
        
'''
# 算术运算符
a = 2
b = 3
c = d = 100
name, age, stu_id = 'Jane', 18, 1001
temp = a ** b
print(type(temp))
print("a ** b: " + str(temp))
print("b / a : " + str(b / a))
print("d // b :" + str(d // b))

# 复合运算符
a += b
print("a += b, a = " + str(a))

# 比较运算符
print("比较运算符：")
i1 = 10
i2 = 20
result = i1 >= i2
print("i1 >= i2 ?? " + str(result))

# 数字之间的逻辑运算
# and运算符
print("数字之间的and运算")
bool_and1 = 1 and 2 and 3
bool_and2 = 1 and 2 and 0
print(bool_and1)
print(bool_and2)

# or运算符
print("数字之间的or运算")
bool_or1 = 1 or 2 or 3 or 0
bool_or2 = 0 or 0 or 8 or 0
bool_or3 = 0 or 0 or 0
print(bool_or1)
print(bool_or2)
print(bool_or3)

