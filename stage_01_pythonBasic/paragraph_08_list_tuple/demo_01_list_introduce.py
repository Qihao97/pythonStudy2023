#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_list_introduce.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/11 0:12    Qihao      1.0         None
'''
# import lib

"""
列表简介：
1. 列表可以一次性存储多个数据，且各个数据可以是不同的数据类型，但是一般推荐使用同一种数据类型，以便操作
2. 列表的格式： [data1, data2, data3...]
3. 对列表的常用操作包括： 增、删、改、查
    (1) 按下标查找， 格式： 列表名[下标]
    (2) index()方法： 返回指定数据所在位置的下标
        列表序列.index(数据, 开始位置, 结束位置)
    (3) count()方法： 统计指定数据在当前列表中出现的次数
        列表序列.count(指定字符串, 开始下标, 结束下标)
    (4) len()方法： 计算指定的列表长度，即列表中数据的个数，返回值是列表长度
        len(目标序列)
        len()方法为公共方法，可以计算列表、元组、字典等长度
4. in 和 not in
    in： 判断指定的数据是否在某个序列，如果在，则返回True，不在则返回False
        给定字符串 in 序列
    not in: 同上，如果不在，则返回True，在则返回False    
"""

# 列表的下标操作
print("列表的下标操作，按下标取数据： ")
list1 = ["hello", "world", "python"]
i = 0
while (i < 3):
    print(list1[i])
    i += 1

print("使用for循环遍历： ")
for l in list1:
    print(l)

# 测试index和count
print("\n测试index和count: ")
list2 = ["hello", "world", "hello", "world", "python", "python", "Python"]
index_sub = list2.index("python")
print(f"list2中，\"{list2[index_sub]}\"的下标为{index_sub}.")
count_list2 = list2.count("python")
print(f"list2中，\"python\"字符串一共出现了{count_list2}次.")
len_list2 = len(list2)
print(f"list2的元素个数，即长度为：{len_list2}")

# 测试in和not in
print("\n测试in和not in : ")
list3 = ["hello", "world", "hello", "world", "python", "python", "Python"]
in_list3 = "hello" in list3
not_in_list3 = "hello" not in list3
print(f"\"hello\"在list3中吗？ -- {in_list3}")
print(f"\"hello\"不在list3中吗？ -- {not_in_list3}")

# 判断邮箱名是否已存在案例
print("判断邮箱名是否已存在案例")
name_list = ["Tom", "Jane", "Jack", "Marry", "Henry"]
name = input("请输入您要注册的名字： ")

if name in name_list:
    print(f"您输入的邮箱名字为{name}，该名字已存在.")
else:
    print(f"您输入的邮箱名字为{name}，该名字未注册，可以使用.")

