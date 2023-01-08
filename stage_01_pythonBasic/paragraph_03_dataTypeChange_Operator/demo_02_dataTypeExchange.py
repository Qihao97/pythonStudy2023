#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_dataTypeExchange.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 12:26    Qihao      1.0         None
'''
# import lib
"""
由于input()方法接收到的数据都是字符串类型的，
在需要使用非字符串类型，如int、float等类型的数据时，需要进行数据类型转换
实践：
1.使用input()方法输入一个整数，用一个变量接收
2.检查输入内容的数据类型
3.使用int()方法做数据类型的转换
4.验证是否转换成功
"""
num = input("Please enter a number:")
print(num)
print("num is " + str(type(num)) + " type.")

# 1. int()方法将数据转换为int类型
print("将输入的数据转换为int类型")
i = int(num)
print(num)
print("num is " + str(type(num)) + " type.")

# 2. float()方法将数据转换为float类型
print("将输入的数据转换为float类型")
f = float(num)
print(f)
print("num is " + str(type(f)) + " type.")

# 3. str()方法将数据转为str类型
print("将输入的数据转换为str类型")
str1 = str(f)
print(str1)
print("str1的类型是： " + str(type(str1)))

# 4.tuple()方法，将一个序列转换为元组
print("使用tuple()方法，将数据转为元组类型")
list1 = [1, 2, 3]
print("list1的类型是： " + str(type(list1)))
tup = tuple(list1)
print("tup 的类型是： " + str(type(tup)))

# 5.list()方法，将一个序列转换为列表
print("使用list()方法，将一个序列转换为列表")
list2 = list(list1)

# 6.eval()方法，计算在字符串中的有效python表达式，并返回一个对象
# 通俗的说就是，将字符串中的数据转为其原本的数据类型
print("使用eval()方法将字符串中的数据转换为其原本的类型")
eval1 = eval("1")
eval2 = eval("1.0")
eval3 = eval("(1, 2, 3)")
eval4 = eval("[1, 2, 3]")
eval5 = eval("{1, 2, 3}")
eval6 = eval("{\"name\" : \"Jane\", \"age\" : 18}")
print(type(eval1))
print(type(eval2))
print(type(eval3))
print(type(eval4))
print(type(eval5))
print(type(eval6))


