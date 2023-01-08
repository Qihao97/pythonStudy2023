#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_inputBasic.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 11:34    Qihao      1.0         None
'''
# import lib
"""
输入的语法：
input("提示信息")
input("")方法的特点：
1.当python程序执行到input的时候，要等待用户输入，输入之后，程序才继续向下执行
2.在python中，一般用一个变量来接收input方法输入的内容
3.在python中，input方法会把用户输入的任何内容都当作字符串来处理
"""
text = input("请输入文本：")
print("您输入的文本是：" + text)