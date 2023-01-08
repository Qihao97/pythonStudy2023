#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_dataTypeBasic.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 8:39    Qihao      1.0         None
'''
# import lib
"""
python中的数据类型有：
1.数值型，包括int和float
2.布尔类型，true和false
3.字符串类型，str
4.列表，list
5.元组，tuple
6.集合，set
7.字典，dict

实践内容：
1.将不同的变量，存储不同了类型的数据
2.验证这些数据的类型，涉及检测数据类型的知识点，type(变量)
"""

# 定义变量，使用type()函数验证其数据类型
num1 = 1
num2 = 2.1
print(type(num1))   # int -- 整型变量
print(type(num2))   # float -- 浮点型变量

# str -- 字符串类型， 在python中，用英文引号引起来的变量是字符串类型,英文的单引号双引号皆可
str1 = "Hello World!"
print(type(str1))

# bool -- 布尔类型，其值只有True和False
bool1 = True
bool2 = False
print(type(bool1))
print(type(bool2))

# list -- 列表，在python中，使用英文方括号[]括起来的数据，称为列表
list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1))

# tuple -- 元组，在python中，使用英文圆括号()括起来的数据，称为元组
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

# set -- 集合，在python中，使用英文花括号{}括起来的数据，称为集合
set1 = {1, 2, 3, 4, 5}
print(set1)
print(type(set1))

# dict -- 字典，在python中，用英文花括号{}括起来的，内容为键值对的数据，称为字典
dict1 = {"name" : "Tom", "age" : 19, "gender" : "male"}
print(dict1)
print(type(dict1))
