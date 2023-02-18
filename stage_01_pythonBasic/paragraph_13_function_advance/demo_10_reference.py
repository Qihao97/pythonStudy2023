#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_10_reference.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/18 18:16    Qihao      1.0         None
'''
# import lib
"""
在python中，值是靠引用来传递的
可以使用id()来判断两个变量是否为同一个值的引用，可将id理解为所在内存的标识
"""

# 不可变类型，以int类型为例
a = 1
b = a
# 此时a和b的id相同
print(id(a))
print(id(b))

print("--*-" * 12)
b = 2
# 此时b获得了新的id，a的地址和值都不变
print(a)
print(id(a))
print(id(b))

# 列表测试：可变数据类型
print("--*-" * 12)
aa = [10, 20]
bb = aa
print(aa)
print(bb)

print(id(aa))
print(id(bb))

print("--*-" * 12)
# 修改aa的数据
# 修改了其中一个的内容，两个的内存地址都不变，且数据同步更改
aa.append(30)
print(aa)
print(bb)
print(id(aa))
print(id(bb))

