#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_10_input_output.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/5/31 10:16    Qihao      1.0         None
'''
# import lib
"""
1. 字符串输入：
    可以使用input()函数接收从键盘输入的字符串，该函数返回值为键盘接收到的字符串；
    括号里可以写提示信息
2. 字符串输出：
    两种输出方式：
    print("****%s" %v)
    print(f"****{v}***")
3. 使用eval()函数可以将字符串中的数据转成其本来的数据类型
4. 使用type()函数可以检测变量类型
"""
str1 = input("Please enter a string: ")
print("This string is: %s" %str1)
print(f"This string is : {str1}")

str2 = input("请输入一个int类型的数据： ")
i = eval(str2)
print("输入的类型为： %s" %type(str2))
print(f"转换后的类型为： {type(i)}")
print(f"转换后的值为： {i}")
