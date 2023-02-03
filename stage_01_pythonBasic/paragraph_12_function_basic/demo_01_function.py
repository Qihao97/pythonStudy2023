#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_function.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/2 23:32    Qihao      1.0         None
'''
# import lib
"""
函数体验
定义函数：
def 函数名(参数):
    函数体
    ...

调用函数：
函数名(参数)

函数需要先定义再使用，根据实际情况，参数可有可无
"""

# 复现ATM机器取钱

# 确定选择功能页面：显示余额、存款、取款
def sel_func():
    print("显示余额")
    print("存款")
    print("取款")

# 搭建整体框架：输入密码登陆后显示功能，查询余额后显示功能，取款后显示功能

print("恭喜登录成功！")
sel_func()

print("您的余额为：$100，000，000")
sel_func()

print("取了$1000")
sel_func()