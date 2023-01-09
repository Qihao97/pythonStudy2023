#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_index_introduce.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 21:13    Qihao      1.0         None
'''
# import lib
"""
下标：
1. 在程序运行过程中，数据存储在内存中
2. 在字符串或者列表、元组等数据结构中，这些数据将从0开始被分配一个标号，使用
   这些编号可以很方便很精确找到某个数据，这种编号称为下标、索引或者索引值
"""
# 索引示例
print("利用字符串的索引精确找到某个字符")
str1 = "HelloWorld!"
print(str1)
print(f"字符串 {str1} 中，索引为1的字符是{str1[1]}.")


