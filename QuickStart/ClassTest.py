#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '''
    所有员工的基类
    所有员工的基类
    '''
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

class Point:
    def __int__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"

class Parent:
    parentAttr = 100

    def __init__(self):
        print "父类构造"

    def parentMethod(self):
        print "父类方法"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性: ", Parent.parentAttr

    def sameMethod(self):
        print "都有的方法：父类"

class Child(Parent):
    def __init__(self):
        print "子类构造方法"
        print "需要显示调用父类构造方法，要加self参数"
        Parent.__init__(self)

    def childMethod(self):
        print "子类方法"

    def sameMethod(self):
        print "都有的方法：子类"
        print "调用父类方法一定要加self参数"
        Parent.sameMethod(self)

class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount