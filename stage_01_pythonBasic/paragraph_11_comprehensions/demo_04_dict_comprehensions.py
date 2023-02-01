#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_dict_comprehensions.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/31 22:08    Qihao      1.0         None
'''
# import lib

"""
字典推导式：
快速合并列表为字典，或者提取字典中目标数据
"""
# 创建一个字典，key为1到5的数字，value为key的平方
dict1 = {i : i ** 2 for i in range(1, 5)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16}

# 合并两个列表为一个字典
# 如果两个列表的长度相同，len可以统计任意一个，
# 如果不同，统计短的那个，否则报错
list1 = ["name", "age", "gender"]
list2 = ["Lisa", 18, "female"]
dict2 = {list1[i] : list2[i] for i in range(len(list1))}
print(dict2) # {'name': 'Lisa', 'age': 18, 'gender': 'female'}

# 提取字典中的目标数据
print(("-" * 9) + ("*" * 5) + ("-" * 9))
print("提取字典中的目标数据")
counts = {"MBP" : 128, "Lenovo" : 256, "acer" : 208, "DELL" : 202, "HP" : 188, "ASUS" : 122}

# 需求：提取上述集合中，电脑数量大于等于200的字典数据
count1 = {key : value for key, value in counts.items() if value >= 200}
print(count1)


