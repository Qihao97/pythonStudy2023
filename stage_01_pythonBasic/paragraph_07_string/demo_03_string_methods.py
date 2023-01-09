#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_string_methods.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 22:49    Qihao      1.0         None
'''
# import lib
"""
python字符串的常用操作方法：
1. 字符串常用的操作方法主要有查找、修改、判断三种
2. 查找：查找子串在字符串中的位置或者出现的次数
    find方法：检测某个子串是否包含在目标字符串中，如果包含，返回其开始位置下标，否则返回-1
    语法： 字符串序列.find(子串, 开始位置下标, 结束位置下标)  -- 开始和结束位置的下标可以省略，表示从整个字符串序列中查找
    index(): 检测某个子串是否包含在目标字符串中，如果包含，返回这个子串开始位置的下标，否则报异常
    语法： 字符串序列.index(子串, 开始位置下标, 结束位置下标)  -- 开始和结束位置的下标可以省略，表示从整个字符串序列中查找
    count(): 计算某个子串在目标字符串中出现的次数并返回
    语法： 字符串序列.count(子串, 开始位置下标, 结束位置下标)
"""
# 字符串查找方法
mystr = "hello world and itcast and itheima and Python"

# 1. 使用find()方法查找
print("使用find()方法进行查找：")
print(mystr.find("and"))    # 输出12，为该子串首次出现的下标位置
print(mystr.find("and", 15, 30))    # 输出23，带上开始和结束下标，只在圈定的范围内查找
print(mystr.find("ands"))   # 输出-1， 尝试在字符串中查找一个不存在的子串，返回-1

# 2. 使用index()方法进行查找
print("使用index()方法进行查找: ")
print(mystr.index("and"))   # 输出12，为该子串首次出现的下标位置
# print(mystr.index("ands"))  # 报错，程序终止，使用index()方法查找不存在的子串，会报错

# 3. 使用count()方法进行计数
print("使用count()方法进行计数: ")
print(mystr.count("and", 15, 30))    #输出1, 计算下标15到30之间"and"的个数
print(mystr.count("and"))   # 输出3， 不写开始和结束下标，默认是从全字符串查找
print(mystr.count("ands"))  # 输出0， 在目标字符串中找不到，count()方法返回0

# 4. rfind()和rindex()， 用法和find、index方法类似，但是查找方式是从右边开始
print(mystr.rfind("and"))   # 输出35， 从右侧开始查找，返回的下标是正常的，从左向右的下标
print(mystr.rindex("and"))  # 输出35，同上
# print(mystr.rindex("ands")) # 同index()方法，找不到的时候报错，程序终止


