#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_09_string_introduce.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/5/31 9:48    Qihao      1.0         None
'''
# import lib

'''
1. 认识字符串：
    字符串可以使用''、""、''''''、""""""定义，
    其中使用三个引号定义的，定义的时候什么样，输出就是什么样，
    换行之后不带\，使用两个引号定义的需要，换行行书写也默认不带换行

'''

str1 = 'Hello World!'
str2 = '''Hello  w
        orld!'''
str3 = 'Hello W' \
       'orld!'

print(str1)
print(str2)
print(str3)

