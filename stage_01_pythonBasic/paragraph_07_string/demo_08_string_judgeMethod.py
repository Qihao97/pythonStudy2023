#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_08_string_judgeMethod.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/10 23:19    Qihao      1.0         None
'''
# import lib

"""
Python字符串的判断方法：
1. isalpha(): 如果字符串至少有一个字符且所有字符都是字母，则返回True，否则返回False
    语法： 目标字符串.isalpha()
2. isdigit(): 同上，判断字符串是否是纯数字
3. isalnum(): 同上，判断字符串是否只含数字和字母
4. isspace(): 同上，判断字符串是否只含空格
"""

# 测试isalpha方法
print("测试isalpha方法: ")
alpha_str = "abcdefg"
print(f"测试字符串： {alpha_str}")
alpha_bool = alpha_str.isalpha()
print(alpha_bool)

# 测试isdigit方法
print("测试isdigital方法: ")
digit_str = "123456"
print(f"测试字符串： {digit_str}")
digit_bool = digit_str.isdigit()
print(digit_bool)

# 测试isalnum方法
print("测试isalnum方法: ")
alnum_str = "abcdefg123456"
print(f"测试字符串： {alnum_str}")
alnum_bool = alnum_str.isalnum()
print(alnum_bool)

# 测试isspace方法
print("测试isspace方法: ")
space_str = "    "
print(f"测试字符串： {space_str}")
space_bool = space_str.isspace()
print(space_bool)
