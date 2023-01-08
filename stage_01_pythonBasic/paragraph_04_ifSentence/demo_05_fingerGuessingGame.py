#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_05_fingerGuessingGame.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/8 23:38    Qihao      1.0         None
'''
# import lib
import random
"""
使用if语句做一个猜拳游戏
步骤：
1.出拳
    玩家：手动输入
    电脑：1.固定出剪刀 2.随机出
2.判断输赢
    2.1 玩家获胜
    2.2 平局
    2.3 电脑获胜
"""

"""
使用随机数
1. 导入random模块： import random
2. 使用该模块的方法： random.randint()括号内输入开始数字和结束数字即可，该方法包含开始和结束
"""
# 玩家
player = int(input("请出拳 0--石头， 1--剪刀， 2--布： "))
# 电脑
# computer = 1
computer = random.randint(0, 2)
print(f"电脑出拳： {computer}")
# 判断输赢
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)) :
    print("玩家获胜，哈哈哈")
elif (player == computer):
    print("平局，别走，再来一局")
else:
    print("电脑获胜")


