#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_02_whileLoop_apply.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 11:42    Qihao      1.0         None
'''
# import lib

"""
循环的简单应用，1到100之间的整数累加
"""
i = 1
result = 0
while (i <= 100):
    result += i
    i += 1
print(result)

"""
使用条件判断来做1到100之间的偶数累加求和
比较推荐
"""
print("使用条件判断来做1到100之间的偶数累加求和")
i1 = 1
result1 = 0
while (i1 <= 100):
    if (i1 % 2 == 0) :
        result1 += i1
    i1 += 1

print(result1)

"""
使用计数器控制步长，求1到100之间偶数的和
"""
print("使用计数器控制步长，求1到100之间偶数的和")
i2 = 0
result2 = 0
while (i2 <= 100):
    result2 += i2
    i2 += 2
print(result2)
