#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_06_range.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/29 22:42    Qihao      1.0         None
'''
# import lib

"""
range(start, end, step): 生成从start到end的可迭代数字对象，可供for循环使用
默认step为1，生成的数字包含start不包含end
"""

# 1	2	3	4	5	6	7	8	9
for i in range(1, 10, 1):
    print(i, end="\t")
print()

# 1 3	5	7	9
for i in range(1, 10, 2):
    print(i, end="\t")
print()

# 0	1	2	3	4	5	6	7	8	9
# 默认从0开始，步长为1
for i in range(10):
    print(i, end="\t")
print()

