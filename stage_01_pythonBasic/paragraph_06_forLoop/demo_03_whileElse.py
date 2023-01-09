#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_whileElse.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 20:27    Qihao      1.0         None
'''
# import lib
"""
while语句可以和else语句配合使用，
else下方缩进的代码是当循环正常结束之后要执行的代码

步骤：
1. 书写正常的循环
2. 循环正常结束后要执行的代码 -- else

结论：
1. 循环执行break语句退出，下方else缩进下的语句不执行
2. 因为continue是退出当前一次循环，继续下一次循环，因此不影响该循环正常退出，当循环正常结束后，下方else缩进下的代码仍可执行
"""
print("测试break语句")
i = 0
while (i < 5):
    print("Hello World!")
    i += 1
    if(i == 4):
        # 如果执行到该break语句，下面else缩进下的语句则不执行
        break
else:
    print("Success!")

# 测试continue语句
print("测试continue语句")
j = 0
while (j < 5):
    print("Hello World!")
    j += 1
    if (j == 3):
        print("这次算了，下次一定!")
        # 执行到continue语句，可以正常退出循环，else缩进下的语句仍可执行
        continue
else:
    print("Success!")