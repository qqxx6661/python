# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib
import urllib2
import re
import sys
import socket
import os

class Tool:
    removeExtraTag = re.compile(r'_cke_saved_src="http.+?.jpg')     #某些页面有多余字符
    def replace(self,x):
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()    #strip()将前后的多余内容删除

class Spider:
 
    def __init__(self,siteURL):
        self.siteURL = siteURL
        
    def getPage(self,pageIndex):
        if pageIndex == 1:
            url = self.siteURL + ".shtml"
        else:
            url = self.siteURL + "_" + str(pageIndex) + ".shtml" 
        print '准备抓取：' + url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    def getPic(self,pageIndex):
        page = self.getPage(pageIndex)
        imgre = re.compile(r'src="(http.+?.jpg)">')     #适合传统抓取
        #imgre = re.compile(r'"http.+?\.shtml\?(http.+?\.jpg)">')   #高清壁纸支持,偶尔会有bug
        imglist = re.findall(imgre,page)
        #print imglist
        imglist_clr = []    #存放清洗过的img地址
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
            except socket.timeout as e:  
                    print "下载超时，跳过此图: %r" % e
                    continue
            x+=1


socket.setdefaulttimeout(5.0)   #设置全局超时5秒
tool=Tool()
print '请输入游民星空网址:'
inURL = raw_input()
inURL = inURL[:-6]  #去除.shtml
li = re.findall(r"\d+\/?\d*",inURL)  #为为文件夹命名
name = li[0]    #li是一个list，取出其中唯一一个字符串
print '图片保存在当前目录的：%s下' % name
if not os.path.exists('%s' % name):#创建目录，有就不创建
    os.makedirs('%s' % name)

spider = Spider(inURL)
for x in range(1,20):
    try:
        spider.getPic(x)
    except urllib2.URLError,e:
        print '服务器报出错误：%s' % e.code
        print '已经没有下一页了'
        break;
print '所有图片保存完毕'
