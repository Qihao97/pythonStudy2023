#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_01_studentManegementSystem.py    
@Contact :   qihao_97@163.com
@License :   (C)Copyright 2022-2023, Qihao

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/20 21:01    Qihao      1.0         None
'''
# import lib

"""
需求：进入系统后，显示系统功能界面，功能包括：
1. 添加学员
2. 删除学员
3. 修改学员信息
4. 查询学员信息
5. 显示所有学员信息
6. 退出系统

步骤分析：
1. 显示功能界面
2. 用户输入功能序号
3. 根据用户输入的功能序号，执行不同的功能（调用不同的函数）

"""

# 定义功能界面函数
def info_print():
    print('请选择功能--------------')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出系统')
    print('-' * 20)

# 系统功能需要循环使用，直到用户输入6，才退出系统
while True:
    # 1. 显示功能界面
    info_print()

    # 2. 用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    # 3. 按照用户输入的功能序号，执行不同的功能(函数)
    # 如果用户输入1，执行添加；如果用户输入2，执行删除... -- 多重判断
    if user_num == 1:
        print('添加')
    elif user_num == 2:
        print('删除')
    elif user_num == 3:
        print('修改')
    elif user_num == 4:
        print('查询')
    elif user_num == 5:
        print('显示所有')
    elif user_num == 6:
        print('退出系统')
        # 程序要想结束，退出终止while True -- break
        exit_flag = input('确定要退出吗？yes or no:  ')
        if exit_flag == 'yes':
            break
    else:
        print('输入的功能序号有误')


