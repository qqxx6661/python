# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib
import urllib2
import re
import sys
import socket
import os

class Tool:
    removeExtraTag = re.compile(r'_cke_saved_src="http.+?.jpg')
    def replace(self,x):
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()    #strip()将前后多余内容删除

class Spider:
 
    def __init__(self,siteURL):
        self.siteURL = siteURL
        
    def getPage(self,pageIndex):
        if pageIndex == 1:
            url = self.siteURL + "?see_lz=1"
        else:
            url = self.siteURL + "?see_lz=1&pn=" + str(pageIndex)
        print '准备抓取：' + url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    def getPic(self,pageIndex):
        page = self.getPage(pageIndex)
        imgre = re.compile(r'<img class="BDE_Image".*?height=".*?" src="(http://imgsrc.*?jpg)"')
        imglist = re.findall(imgre,page)
        print imglist
        imglist_clr = []
        for imgurl in imglist:
            imgurl_clr = tool.replace(imgurl)
            imglist_clr.append(imgurl_clr.encode('utf-8'))  #去除u'
        print '清洗多余字符完成'
        print imglist_clr
        x = 0
        for imgurl_clr in imglist_clr:
            print '正在保存第%s页的第%s张'%(pageIndex,x+1)
            try:
                urllib.urlretrieve(imgurl_clr,'%s/picture_%s_%s.jpg' % (name,pageIndex,x+1))
            except urllib2.URLError, e:  
                if isinstance(e.reason, socket.timeout):  
                    raise MyException("下载超时，跳过此图: %r" % e)
                    continue
                else:
                    continue
            x+=1


socket.setdefaulttimeout(5.0)   #设置全局超时5秒
tool=Tool()
print '请输入百度帖子网址:'
inURL = raw_input()

li = re.findall(r"\d+",inURL)
name = li[0]#li是一个list，取出其中唯一一个字符串
print '图片保存在当前目录的：%s下' % name
if not os.path.exists('%s' % name):
    os.makedirs('%s' % name)

spider = Spider(inURL)
for x in range(1,30):
    try:
        spider.getPic(x)
    except urllib2.URLError,e:
        print '服务器报出错误：%s' % e.code
        print '已经没有下一页了'
        break;
print '所有图片保存完毕'
