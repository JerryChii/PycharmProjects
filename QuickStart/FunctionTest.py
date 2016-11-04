#!/usr/bin/python
# -*- coding: UTF-8 -*-

print '======================================'

# 给变量赋初值
def printinfo(name, age = 10):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age ", age
    return


# 指定变量名赋值
printinfo(age=50, name="miki")


# 不定长参数
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

print '======================================'
#lambda

sum = lambda arg1, arg2 : arg1 + arg2

print sum("a", "b")

print '======================================'
import sys
print sys.path

# !/usr/bin/python
# -*- coding: UTF-8 -*-

print '======================================'
Money = 2000

def AddMoney():
    #Money += 1是一个表达式，这说明默认已经声明了一个局部变量Money
    # 想改正代码就取消以下注释:
    global Money
    Money += 1


print Money
AddMoney()
print Money

#或者这样
def AddMoney():
    Money = 1
    Money += 1

print Money
AddMoney()
print Money

print '======================================'
import math

content = dir(math)
print content

print '======================================'
tetkk = 100
def tet():
    kk = 1
    print globals().keys()
    print locals().keys()

tet()