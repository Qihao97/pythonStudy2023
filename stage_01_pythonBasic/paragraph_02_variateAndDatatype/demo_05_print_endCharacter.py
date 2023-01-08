#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_05_print_endCharacter.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 11:22    Qihao      1.0         None
'''
# import lib
'''
print()方法默认在最后带一个'\n'字符，即输出后自动换行，
print()方法的结束符可以修改，格式如下：print("str1", end = "str2")
'''
print("Hello World!", end="\t")
print()
print("Hello World!", end = "end")
print()
print("Hello World!", end = "...")
print("Hello World!")
