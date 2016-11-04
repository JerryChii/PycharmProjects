#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ClassTest import Employee

emp1 = Employee("Zara", 2000)
emp1.displayCount()
emp1.displayEmployee()

emp2 = Employee("Manni", 5000)
emp2.displayCount()
emp2.displayEmployee()

print Employee.empCount

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

#添加属性
emp1.age = 7
print emp1.age

del emp1.age


#####对象收集机制
print "#####" * 4
from ClassTest import Point
pt1 = Point()
pt2 = pt1
pt3 = pt1

print id(pt1), id(pt2), id(pt3)
del pt1
del pt2
del pt3

#继承
from ClassTest import Parent, Child

print "#####" * 4
c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

c.sameMethod()

#私有属性、方法
from ClassTest import JustCounter

print "#####" * 4
counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#object._className__attrName可以这样访问
print counter._JustCounter__secretCount