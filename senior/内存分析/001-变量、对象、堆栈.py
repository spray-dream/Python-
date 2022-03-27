# -*- coding = utf-8 -*-
# @Time : 2021/4/25 09:07
# @Author : spray_dream
# @File : 变量、对象、堆栈.py
# @Software: PyCharm
"""
1、对象拥有地址,类型,和值.当把值赋给变量时,相当于将对象的地址,类型等引向了变量,而调用变量时指向了对象.
2、对象的本质就是一个内存块.变量也是对象的引用.变量存储的是对象的地址,变量通过地址"引用"了对象
3、变量位于栈内存，对象位于堆内存
4、把变量删了，只是把引用“地址”这个动作给删除了。如果对象没有变量引用，就会被垃圾回收器回收，清理内存空间
5、变量第一次被赋值就是初始化，使用前必须要初始化，和JS不同
"""

a = 3.14
print("a的地址是：{}".format(id(a)))
b = int(a)    # 生成一个新的对象，并把它的地址给了b,没有对象的变量会被回收
print(a)
print("b的地址是：{}".format(id(b)))
print("3的地址是：{}".format(id(3)))    # b和c的地址相同


a = b = c = 0
a = 1
print(a, b, c)
d = e = f = []
e.append(0)
print(d, e, f)
