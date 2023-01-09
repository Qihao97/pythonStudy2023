#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_stringMethods_modify.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 23:54    Qihao      1.0         None
'''
# import lib
"""
python字符串常用方法之修改字符串方法
1. replace(): 用一个新的子串来替换旧的子串，不改变原字符串，返回一个新的字符串
    数据根据是否可以改变分为可变类型和不可变类型
    语法： 字符串序列.replace(旧子串, 新子串, 替换次数) -- 如果替换次数如果超出子串实际出现的次数，则按子串实际出现的次数进行替换
    该方法将返回一个按规则替换过的字符串，但是不改变原字符串，因此需要定义一个新的变量来接收经过处理过的字符串
2. split(): 按照指定的字符分割字符串，返回一个列表
    语法： 字符串序列.split(分割字符, num)  --  num表示分割字符出现的次数，即返回的数据个数应为num+1
    该方法会丢失分割字符
3. join(): 合并列表里的字符串数据为一个大的字符串
    语法： 字符或子串.join(多个字符串组成的序列)  --  这里的字符或者字符串就是用来将序列里的字符串连接起来的字符串
4. capitalize(): 将字符串第一个字母转换为大写
    语法： 目标字符串.capitalize()
5. title(): 将字符串的每一个单词的首字母转为大写
    语法： 目标字符串.title()
6. lower(): 将字符串中所有的大写字母转为小写字母
    语法： 目标字符串.lower()
7. upper(): 将字符串中所有的小写字母转为大写字母
    语法： 目标字符串.upper()
"""
mystr = "hello world and itcast and itheima and Python"

# 测试replace()方法
print("测试replace()方法: ")
print(mystr.replace("and", "he"))   # 输出 hello world he itcast he itheima he Python
# replace()方法并不改变原字符串，字符串类型是不可变的数据类型
print(mystr)

# 测试split()方法
print("测试split()方法: ")
print(mystr.split("and", 3))    # 输出 ['hello world ', ' itcast ', ' itheima ', ' Python']
list1 = mystr.split("and")      # 丢失分割字符，输出的内容没有 and
print(list1)

# 测试join()方法
print("测试join()方法")
mylist = ["hello", "world", "itcast", "itheima"]
joinstr = " and ".join(mylist)      # " and " 就是用来将列表中的字符串拼接起来的子串
print(joinstr)

# 测试capitalize()方法 -- 将字符串的首字母转为大写
print("测试capitalize()方法")
mystr1 = "hello and world and itcast and itheima"
newstr1 = mystr1.capitalize()
print(newstr1)

# 测试title()方法 -- 将字符串的每个单词的首字母转为大写
print("测试title()方法")
titleStr = mystr1.title()
print(titleStr)

# 测试lower()方法 -- 将字符串中的大写字母转为小写字母
print("测试lower()方法")
str2 = "Hello World and PYTHON"
lower_str = str2.lower()
print(lower_str)

# 测试upper()方法 -- 将字符串中的小写字母转为大写字母
print("测试upper()方法")
str3 = "hello world and Python."
upper_str = str3.upper()
print(upper_str)
