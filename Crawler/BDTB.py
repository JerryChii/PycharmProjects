# -*- coding:utf-8 -*-
import urllib2
import urllib
import re

class BDTB:
    baseUrl = 'http://tieba.baidu.com/p/'
    def __init__(self, articleNum, seeLZ):
        self.articleNum = articleNum
        self.seeLZ ='?see_lz='+str(seeLZ)

    def getPage(self, pageNum):
        try:
            url = self.baseUrl + str(self.articleNum) + self.seeLZ + '&pn=' + str(pageNum)
            print url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败,错误原因", e.reason
                return None

    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1)
        else:
            return None

bdtb = BDTB(3138733512, 1)
# print bdtb.getPage(1)
print bdtb.getTitle()
