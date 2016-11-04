# -*- coding:UTF-8 -*-
import urllib2
import urllib
import re

page = 1
url = "http://www.qiushibaike.com/hot/page/" + str(page)
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {"User-Agent": user_agent}
content = ""
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile(
        '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?"content".*?span>(.*?)</span>.*?number">(.*?)</.*?number">(.*?)</.*?<div class="cmtMain">.*?</div>',
        re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item[0]
        print item[1]
        print item[2]
        print item[3]
        print "=" * 50
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

