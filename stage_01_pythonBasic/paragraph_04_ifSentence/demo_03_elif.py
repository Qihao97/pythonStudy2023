#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_elif.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 22:53    Qihao      1.0         None
'''
# import lib
"""
多重判断：
语法：
if 条件1:
    条件1成立时要执行的语句
    ...
elif 条件2:
    条件2成立时要执行的语句
    ...
...
else:
    以上条件都不成立时要执行的语句
    ...
    
多重判断的else语句放在最后，表示以上条件都不成立时执行的代码
"""

"""
需求：
    如果年龄小于18，属于童工，不合法
    年龄在18到60之间，属于合法工作年龄
    年龄大于60，应当退休

步骤：
    1.用户在键盘输入年龄 -- 保存变量，转换类型
    2.判断用户的年龄
    3.输出一些提示信息：您输入的年龄为*，是否合法 
"""

age = int(input("请输入您的年龄："))

if (age < 18):
    print(f"您输入的年龄为{age}， 为童工，不合法.")
# elif (age >= 18) and (age <= 60): # 可以化简如下:
elif 18 <= age <= 60:
    print(f"您输入的年龄为{age}， 为法定工作年龄，合法.")
else:
    print(f"您输入的年龄为{age}， 该退休啦.")


