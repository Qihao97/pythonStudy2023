#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_06_while_for_each.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/15 12:29    Qihao      1.0         None
'''
# import lib
'''
列表的遍历，while和for
1. 遍历：依次按顺序访问到列表的每一个元素
2. 使用while循环方式遍历列表：
    i = 0
    while i < len(list):
        print(list[i])
        i += 1
'''

# 使用while循环遍历列表
list1 = ["hello", "world", "python"]
print(f"使用while循环遍历列表: {list1}")
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
print("遍历完毕！")

# 使用for循环遍历列表，遍历序列优先选择for循环
print(f"使用for循环遍历列表: {list1}")
for i1 in list1:
    print(i1)
print("遍历完毕！")

