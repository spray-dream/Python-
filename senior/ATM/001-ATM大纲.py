# -*- coding = utf-8 -*-
# @Time : 2022/2/13 17:39
# @Author : spray_dream
# @File : 001-ATM大纲.py
# @Software: PyCharm

"""
主要功能:
    1.注册:用户名,手机号,身份证号(18位),密码(两次确认,不低于六位)
    2.查询:通过账号进行查询,账号必须存在,密码三次之内输入正确.否则锁定
    3.取款:账号必须存在,密码三次之内输入正确.否则锁定,取款金额不能大于存款
    4.存款:账号必须存在,密码三次之内输入正确.否则锁定,存款金额不能低于0
    5.转账:账号必须存在,转款账户也存在,密码三次之内输入正确.否则锁定,转帐金额不能超过余额
    6.锁卡:账号必须存在,可以使用密码冻结,还能使用身份证号冻结
    7.解卡:账号必须存在,只能使用身份证号解锁
    8.补卡:使用身份证进行补卡,要求每个身份证只能有一张卡,之前的卡作废
    9.改密:使用原密码进行改密,也可以使用身份证号进行改密
    0.退出:保存数据
    扩展功能:交易记录
    注意事项:身份证号和用户名唯一,手机号不限
"""

"""
    卡号:     card_id
    密码:     code
    余额:     money
    是否锁卡: is_lock
    用户名:   name
    身份证号: user_id
    手机号:   phone
    卡对象:   card
    1.注册:register
    2.查询:query
    3.取款:get
    4.存款:add
    5.转账:transfer
    6.锁卡:lock
    7.解卡:unlock
    8.补卡:new_c
    9.改密:change
    0.退出:save
    视图对象:View
"""
