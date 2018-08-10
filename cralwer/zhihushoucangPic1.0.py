# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib
import urllib2
import re
import socket
import os


class Spider:

    def __init__(self, site_url):
        self.site_url = site_url
        self.p = 0

    def get_page(self):
        proxy = {'http': '115.215.209.77:8118'}
        proxy_support = urllib2.ProxyHandler(proxy)
        print proxy_support
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        i_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'}

        self.p += 1
        url = self.site_url + "?page=" + str(self.p)
        print url
        request = urllib2.Request(url, headers=i_headers)
        response = urllib2.urlopen(request)
        return response.read()

    def get_pic(self):
        while 1:
            page = self.get_page()
            img_re = re.compile(r'data-original=&quot;(https://.*?)&')
            img_list = re.findall(img_re, page)
            print 'img_list'
            print img_list
            if img_list:
                x = 1
                for img_url in img_list:
                    print '正在保存第%s页的第%s张'%(self.p, x+1)
                    try:
                        urllib.urlretrieve(img_url,'%s/picture_%s_%s.jpg' % (name, self.p, x))
                    except urllib2.URLError, e:
                        if isinstance(e.reason, socket.timeout):
                            raise MyException("下载超时，跳过此图: %r" % e)
                            continue
                        else:
                            continue
                    x += 1
            else:
                break


print '请输入收藏夹代号:'
in_URL = raw_input()
in_URL = in_URL.strip()
li = re.findall(r"\d+", in_URL)
name = li[0]  # li是一个list，取出其中唯一一个字符串
print '图片保存在当前目录的：%s下' % name
if not os.path.exists('%s' % name):
    os.makedirs('%s' % name)

spider = Spider(in_URL)
spider.get_pic()
print '所有收藏夹内图片保存完毕'
