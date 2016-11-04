# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import Tool

class BDTB:

    def __init__(self, articleNum, seeLZ):
        self.baseUrl = 'http://tieba.baidu.com/p/'
        self.articleNum = articleNum
        self.seeLZ ='?see_lz='+str(seeLZ)
        self.tool = Tool.Tool()

    def getPage(self, pageNum):
        try:
            url = self.baseUrl + str(self.articleNum) + self.seeLZ + '&pn=' + str(pageNum)
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
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?><span.*?<span.*?>(\d+)</span>', re.S)

        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>')
        items = re.findall(pattern, page)
        floor = 1
        if items:
            for item in items:
                print floor, '楼','-' * 80
                print self.tool.replace(item)
                floor += 1
        else:
            None



bdtb = BDTB(3138733512, 1)
# print bdtb.getPage(1)
# print bdtb.getTitle()
# print bdtb.getPageNum()
bdtb.getContent(bdtb.getPage(1))