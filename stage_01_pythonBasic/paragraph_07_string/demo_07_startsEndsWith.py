#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_07_startsEndsWith.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/10 11:07    Qihao      1.0         None
'''
# import lib

"""
判断字符串是否以某个字符串开头或结尾：
1. startswith():  检查字符串是否以指定的子串开头，是则返回True，否则返回False，可设置开始结束位置下标
    语法：  字符串序列.statswith(子串, 开始位置下标, 结束位置下标)
2. endswith():  同上，检查字符串是否以指定的字符串结尾
"""
mystr = "hello world and itheima and python"

# 测试startswith方法
print("测试startswith方法")
startswith_bool = mystr.startswith("hello")
print(startswith_bool)

# 测试endswith方法
print("测试endswith方法")
endswith_bool = mystr.endswith("python")
print(endswith_bool)
