#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_04_forElse.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 20:44    Qihao      1.0         None
'''
# import lib
"""
for-else语句语法：
for 临时变量 in 序列：
    循环体
    ...
else:
    for循环正常退出后要执行的代码
同样也是遇到执行break结束循环时，不执行else缩进的代码，而continue则不影响
"""
print("测试for-else语句.")
str = "hellodemo"
for i in str:
    print(i)
else:
    print("Success!")

# 测试for-else语句和break语句
print("测试for-else语句和break语句")
for i in str:
    if (i == 'm'):
        print("不打印'm'")
        break
    print(i)
else:
    print("Success!")

# 测试for-else语句和continue语句
print("测试for-else语句和continue语句")
for i in str:
    if(i == 'm'):
        print("不打印'm'，继续执行")
        continue
    print(i)
else:
    print("Success!")
