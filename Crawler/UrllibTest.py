#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import urllib
import cookielib

response = urllib2.urlopen("http://cuiqingcai.com/947.html")
print "#"*50
print response.read()

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print "#"*50
print response.read()

values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print "#"*50
print response.read()

url = "http://passport.csdn.net/account/login"
getUrl = url + "?" + data
request = urllib2.Request(getUrl)
response = urllib2.urlopen(request)
print "#"*50
print getUrl
print response.read()

url = "http://wwww.xxxx.com"
request = urllib2.Request(url)
try:
    response = urllib2.urlopen(request)
    print response.read
except urllib2.URLError, e:
    print e.reason
print "#"*50

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
print "#"*50

#父类异常写在子类后面
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"
print "#"*50

#对属性判断
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"
print "#" * 50

#cookielib
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value
print "#" * 50

#cookiefile
fileName = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(fileName)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
print "#" * 50

#use cookiefile
cookie = cookielib.MozillaCookieJar()
cookie.load(fileName, ignore_expires=True, ignore_discard=True)
request = urllib2.Request("http://www.baidu.com")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(request)
print response.read()
print "#" * 50