#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_05_delete_space.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/10 8:50    Qihao      1.0         None
'''
# import lib

"""
删除字符串多余的空格字符：
1. lstrip(): 删除字符串左侧空白字符，返回一个修改该后的字符串
    语法： 目标字符串.lstrip()
2. rstrip(): 删除字符串右侧空白字符
3. strip(): 删除字符串两侧空白字符
"""

mystr = "  hello world adn python   "

# 测试lstrip()方法
print("测试lstrip()方法:  ")
lstrip_str = mystr.lstrip()
print(lstrip_str)

# 测试rstrip()方法
print("测试rstrip()方法")
rstrip_str = mystr.rstrip()
print(rstrip_str)

# 测试strip()方法
print("测试strip()方法:  ")
strip_str = mystr.strip()
print(strip_str)
