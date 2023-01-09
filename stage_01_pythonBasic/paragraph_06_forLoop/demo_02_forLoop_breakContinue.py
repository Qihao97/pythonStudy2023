#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_forLoop_breakContinue.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 18:50    Qihao      1.0         None
'''
# import lib

"""
在for循环中使用break语句和continue语句
"""
# 测试break语句，当遇到字符'l'时退出循环
print("测试break语句")
str = "hello"
for i in str:
    if (i == 'l'):
        break
    print(i)

# 测试continue语句，遇到字符'l'时终止本次循环，进行下一次循环
print("测试continue语句")
for i in str:
    if (i == 'l'):
        print("遇到l不打印")
        continue
    print(i)
