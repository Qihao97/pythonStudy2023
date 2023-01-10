#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_list_add_data.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/11 1:07    Qihao      1.0         None
'''
# import lib

"""
往列表中增加数据的方法有：append、extend、insert
这几个方法直接改变目标列表，不需要设置变量接收
1. append(): 往列表的结尾追加数据
    语法： 列表序列.append(数据) -- 列表是可变数据类型，append方法直接在列表的最后追加数据，如果该方法追加的数据是一个序列，则将该序列整个作为一个元素追加到列表
2. extend(): 列表结尾追加数据，如果数据是一个序列，则将此序列的数据逐一添加到列表
    语法： 列表序列.extend(数据) -- 与append()不同在于数据是一个序列的时候，处理方式不同
3. insert(): 在指定位置新增数据
    语法： 列表序列.insert(位置下标, 数据)
"""

my_list1 = ["hello", "world", "python", "2023"]
my_list2 = ["hello", "world", "python", "2023"]
my_list3 = ["hello", "world", "python", "2023"]
add_list = ["i", "love", "Guangzhou"]

print("最初的字符串：")
print(my_list1)
# 测试append方法
print("测试append方法: ")
# 输出 ['hello', 'world', 'python', '2023', ['i', 'love', 'Guangzhou']]
my_list1.append(add_list)
print(my_list1)

# 测试extend方法
print("测试extend方法: ")
# 输出 ['hello', 'world', 'python', '2023', 'i', 'love', 'Guangzhou']
my_list2.extend(add_list)
print(my_list2)

# 测试insert方法
print("测试insert方法: ")
# 输出 ['hello', 'world', 'insert', 'python', '2023']
my_list3.insert(2, "insert")
print(my_list3)
