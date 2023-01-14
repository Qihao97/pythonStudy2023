#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_05_list_copy.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/14 23:52    Qihao      1.0         None
'''
# import lib

"""
复制列表的数据：
copy()方法
用法： list2 = list1.copy()
"""

# 测试copy()方法
print("测试copy()方法：")
list1 = ["hello", "world", "python"]
print(f"list1: {list1}")
list2 = list1.copy()
print(f"list2: {list2}")
