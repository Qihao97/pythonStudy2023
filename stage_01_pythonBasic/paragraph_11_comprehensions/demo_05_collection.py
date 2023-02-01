#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_05_collection.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/1 22:38    Qihao      1.0         None
'''
# import lib

"""
集合推导式
"""
# 创建一个集合，数据为以下列表数据的平方
# 注意集合有去重功能
list1 = [1, 2, 3, 4, 5, 6]
set1 = {i ** 2 for i in list1}
print(set1)

