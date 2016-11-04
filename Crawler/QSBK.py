# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import thread
import time

class QSBK:

    def __init__(self):
        self.pagetIdx = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIdx):
        try:
            url = "http://www.qiushibaike.com/hot/page/" + str(pageIdx)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
            return None

    def getPageItems(self, pageIdx):
        pageCode = self.getPage(pageIdx)
        if not pageCode:
            print "页面加载失败...."
            return None
        pattern = re.compile(
            '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?"content".*?span>(.*?)</span>.*?number">(.*?)</.*?number">(.*?)</.*?<div class="cmtMain">.*?</div>',
            re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0], item[1], item[2], item[3]])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pagetIdx)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pagetIdx += 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            # self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t阅读量:%s\t赞:%s\n%s" %(page,story[0],story[2],story[3],story[1])
        self.loadPage()

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)

        print(u"还有%s页数据" % len(self.stories))

spider = QSBK()
spider.start()