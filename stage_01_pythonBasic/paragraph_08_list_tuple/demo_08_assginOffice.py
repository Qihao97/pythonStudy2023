#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_08_assginOffice.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/15 23:14    Qihao      1.0         None
'''
import random

# import lib

"""
有8位老师，3个办公室，将8位老师随机分配到这3个办公室
1. 准备数据
    8位老师 -- 列表 ，3个办公室 -- 列表，嵌套列表
2. 分配老师到办公室
    随机分配，把老师的名字写入到办公室列表，即办公室列表追加老师名字
3. 验证是否分配成功
    打印办公室详细信息：每个办公室的人数和对应的老师名字
"""

# 1. 准备数据
teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]
offices = [[], [], []]

# 2. 分配老师到办公室，遍历teachers列表，放到办公室列表中随机的列表元素
for name in teachers:
    i = random.randint(0,2)
    offices[i].append(name)

# 3. 验证是否分配成功
i = 0
for office in offices:
    print(f"办公室 {i} 的人数是： {len(office)}, 老师都有： ")
    for name in office:
        print(name, end="\t")
    print()
    i += 1
print(offices)


