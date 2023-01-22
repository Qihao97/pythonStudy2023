#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_06_dictionary_traversal.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/22 18:16    Qihao      1.0         None
'''
# import lib

f"""
字典的循环遍历
1. 遍历字典中的所有key
    for i in dict.keys():
        ...

2. 遍历字典中的所有value
    for i in dict.values():
        ...

3. 遍历字典中的所有键值对
    for i in dict.items():
        ...
        
4. 遍历字典中的所有键值对（拆包）
    for key, value in dict.items():
        ...

"""

dict1 = {"name" : "Jane", "age" : 18, "gender" : "female", "num" : "1001"}

# 1.遍历字典中的所有key
print("遍历字典中的所有key")
for key in dict1.keys():
    print(key)

# 2. 遍历字典序列中的所有values
print("遍历字典序列中的所有values")
for value in dict1.values():
    print(value)

# 3. 遍历字典序列中的所有键值对
print("遍历字典序列中的所有键值对")
for item in dict1.items():
    print(item)

# 4. 遍历字典中的所有键值对（拆包）
print("遍历字典中的所有键值对（拆包）")
# dict1.items()方法返回一个可迭代的元组列表序列，每个元组的第一个元素放在key中，第二个元素放在value中
for key, value in dict1.items():
    # print(key)
    # print(value)
    print(f"{key} : {value}")
