#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_list_change.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/13 23:31    Qihao      1.0         None
'''
# import lib

"""
修改列表，修改元素、逆置、排序
"""

# 修改指定下标的数据
print("修改指定下标的数据: ")
list1 = ["hello", "world", "python"]
print(f"原list1： {list1}")
list1[0] = "Hello!"
print(f"新list1: {list1}")

# 逆序reverse
print("逆序")
# list2 = ["hello", "world", "python"]
list2 = [1, 2, 3, 4, 5, 6]
print(f"原list2：{list2}")
list2.reverse()
print(f"新list2：{list2}")

# 排序sort
print("排序")
list3 = [3, 5, 6, 8, 1, 2, 4, 7, 9]
print(f"原list3： {list3}")
list3.sort()
print(f"新list3： {list3}")


