#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_03_break.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 15:32    Qihao      1.0         None
'''
# import lib
'''
break语句：当某些条件成立，退出整个循环，即终止整个循环
例如循环吃五个苹果，吃完第三个吃饱了，剩下的不吃了（不执行）

'''
i = 1
while (i <= 5):
    # 吃到第4个，吃饱了就不吃了
    if (i == 4):
        print("吃饱了，不吃了.")
        break
    print(f"吃了第{i}个苹果.")
    i += 1


