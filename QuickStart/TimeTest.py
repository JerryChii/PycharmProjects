#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time


localtime = time.localtime(time.time())
print(localtime)

print time.asctime(time.localtime(time.time()))

print time.asctime(time.localtime())

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

import calendar

print calendar.month(2016, 1)

print time.clock()