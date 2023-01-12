#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_list_delete.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/12 22:43    Qihao      1.0         None
'''
# import lib
"""
列表删除数据
del
1. 删除列表： del 列表名
2. 删除指定数据： del 列表名[下标]

pop()： 删除指定下标的数据（默认为最后一个），并返回该数据
语法： 列表序列.pop(下标)

remove(): 移除列表中某个数据的第一个匹配项
语法： 列表序列.remove(数据)

clear(): 清空列表
语法： 目标列表.clear()
"""

# 测试del
print("测试del")
list1 = ["hello", "world"]
print(f"list1: {list1}")
del list1[0]
print(f"del list1[0]: {list1}")
print("del list1:  ")
del list1
# print(list1) 报错，NameError: name 'list1' is not defined
# print(list1)

# 测试pop()方法
print("测试pop()方法: ")
list2 = ["list2", "hello", "world", "python"]
print(f"list2: {list2}")
list2.pop()
print(f"删除最后一个数据后： {list2}")
list2.pop(0)
print(f"再删除第一个数据后： {list2}")

# 测试remove()方法
print("测试remove()方法： ")
list3 = ["hello", "world", "python"]
print(f"list3:  {list3}")
list3.remove("python")
print(f"list3删除\"remove\"之后： {list3}")

# 测试clear()方法
print("测试clear()方法")
list4 = ["hello", "world", "python"]
print(f"list4: {list4}")
list4.clear()
print(f"list4.clear() : {list4}")
