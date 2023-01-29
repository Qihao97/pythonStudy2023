#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_07_enumerate.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/29 22:57    Qihao      1.0         None
'''
# import lib

"""
enumerate(): 用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，
同时列出数据和数据下标，一般用在for循环中
    enumerate(可遍历对象, start = 0)
    start参数用来设置遍历数据的下标起始值，默认为0
"""

list1 = ["a", "b", "c", "d", "e", "f", "g"]
for i in enumerate(list1):
    print(i)
"""
输出：
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
(5, 'f')
(6, 'g')
enumerate()返回的结果是元组的形式，元组的第一个数据是原迭代对象数据对应的下标
第二个数据为原迭代对象的数据，默认start为0，可以手动更改为想要的值
"""

print("*" * 81)
for i in enumerate(list1, start=1):
    print(i)


