#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_06_str_alignment.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/10 9:04    Qihao      1.0         None
'''
# import lib
""""
python中的对齐方法
1. ljust(): 返回一个原字符串的左对齐，并使用指定的字符（默认是空格）进行填充至对应长度的新字符串
    字符串序列.ljust(指定长度， 填充字符)
2. rjust(): 同上，右对齐
3. center(): 同上，居中对齐
"""
mystr = "hello world!"

# 测试左对齐
print("测试左对齐")
ljust_str = mystr.ljust(20, "*")
print(ljust_str)

# 测试右对齐
print("测试右对齐")
rjust_str = mystr.rjust(20, "*")
print(rjust_str)

# 测试居中对齐,不是绝对居中
print("测试居中对齐")
center_str = mystr.center(20, "*")
print(center_str)
