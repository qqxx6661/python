#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: blogyuan.py
@time: 2018/12/7 15:53
"""

import requests
import time
import json
from lxml import etree


def get_blog_yuan(blog_name, header):
    for i in range(1, 6):
        url = 'https://www.cnblogs.com/' + blog_name + '/default.html?page=' + str(i)
        r = requests.get(url, headers=header, timeout=6)
        selector = etree.HTML(r.text)
        names = selector.xpath("//*[@class='postTitle']/a/text()")
        links = selector.xpath("//*[@class='postTitle']/a/@href")
        for num in range(len(names)):
            print(names[num], links[num])
        time.sleep(5)


get_blog_yuan('Java3y', {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                                       'AppleWebKit/536.6 (KHTML, like Gecko) '
                                       'Chrome/20.0.1092.0 Safari/536.6'})
