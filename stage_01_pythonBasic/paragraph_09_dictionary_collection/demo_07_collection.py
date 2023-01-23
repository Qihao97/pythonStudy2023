#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_07_collection.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/23 11:55    Qihao      1.0         None
'''
# import lib

"""
集合及其常见操作
特点：1.集合里的数据不允许重复 2.集合里的元素没有顺序，不能使用下标操作 3.集合属于可变数据类型，可以增删其中数据
1. 创建集合
    创建集合使用{}或者set(),但是创建空集合只能使用set(),因为{}用来创建空字典
    eg： set1 = {1, 2, 3}
    set2 = set()
    set3 = set("abc")
2. 增加数据
    add()方法， 集合序列.add(data)
    因为集合有去重功能，因此若向集合中追加的数据是集合中已有的数据时，将不进行任何操作
    update()方法，追加的数据是序列， 集合序列.update(data)

3. 删除数据
    remove(): 删除集合中的指定数据，如果不存在则报错
    discard(): 删除集合中的指定数据，如果数据不存在，不报错
    pop(): 随机删除集合中的某个数据，并返回这个数据

4. 查找数据
    in: 判断数据在集合序列，返回布尔值
    not in: 判断数据不在集合序列，返回布尔值
"""

# 创建集合
print("创建集合")
set1 = {1, 2, 3, 4, 5}
set2 = set()
set3 = set("abc")
print(set1)
print(set2)
print(set3)

# 集合增加数据
print("集合增加数据")
set4 = {1, 2, 3}
print(set4)
set4.add(100)
print(set4)
list1 = [4, 5, 6]
set4.update(list1)
print(set4)

# 集合删除数据
print("集合删除数据")
set5 = {1, 2, 3, 4, 5}
print(set5)
# 测试remove()方法
set5.remove(5)
print(set5)
# 以下删除元素语句将报错，因为元素5已经被删除
# set5.remove(5)

# 测试discard()方法
print("----------------")
print("测试discard()方法")
print(set5)
set5.discard(4)
set5.discard(4)
set5.discard(4)
print(set5)

# 测试pop()方法
print("测试pop()方法")
print(set5)
p = set5.pop()
print(p)
print(set5)

# 集合查找数据
print("集合查找数据--判断一个数据在不在集合中")
set6 = {"Jane", "Tom", "Jack", "Richard", "Mary"}
print("Jane" in set6)
print("Jane" not in set6)

