#! /usr/bin/python
#运行这行程序会出错,提示你字符串和数字不能连接,于是只好用内置函数进行转换
a=2
b="test"
c=str(a)+b
d="1111"
e=a+int(d)
#How to print multiply values
print ("c is %s,e is %i" % (c,e))

'''
知识点:
    * %标志转换符开始
    * 用int和str函数将字符串和数字进行转换
    * 注释以#开头,而不是习惯的//
    * 打印多个参数的方式
'''
