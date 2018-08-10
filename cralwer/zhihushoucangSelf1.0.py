# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import re
import time
from subprocess import Popen
import mysql.connector

class Spider:

    def __init__(self):
        print '爬虫初始化......'
        self.s = requests.session()

        # 代理信息
        self.proxies = {"https": "https://119.188.94.145:80"}
        try:
            r = self.s.get('http://www.baidu.com/', proxies=self.proxies)
        except requests.exceptions.ProxyError, e:
            print e
            print '代理失效，请修改代码更换代理'
            exit()
        print '代理通过验证，可以使用'

        # 知乎headers
        self.headers = {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.zhihu.com',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
            'Host': 'www.zhihu.com'
        }

        # 登陆知乎获取验证码
        r = self.s.get('http://www.zhihu.com', headers=self.headers, proxies=self.proxies)
        cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags=0)
        strlist = cer.findall(r.text)
        _xsrf = strlist[0]
        #print(r.request.headers)
        #print(str(int(time.time() * 1000)))
        Captcha_URL = 'https://www.zhihu.com/captcha.gif?r=' + str(int(time.time() * 1000))
        r = self.s.get(Captcha_URL, headers=self.headers)
        with open('code.gif', 'wb') as f:
            f.write(r.content)
        Popen('code.gif', shell=True)
        captcha = input('captcha: ')
        login_data = {  # 填写账号信息
            '_xsrf': _xsrf,
            'phone_num': '18769201984',
            'password': 'ybs852421',
            'remember_me': 'true',
            'captcha': captcha
        }
        # 登陆知乎
        r = self.s.post('https://www.zhihu.com/login/phone_num', data=login_data, headers=self.headers, proxies=self.proxies)
        print(r.text)

    def get_collections(self):  # 获取关注的收藏夹
        # 抓取自己创建的收藏夹
        r = self.s.get('https://www.zhihu.com/collections/mine', headers=self.headers, proxies=self.proxies)
        # 抓取关注的收藏夹
        #r = self.s.get('https://www.zhihu.com/collections', headers=self.headers, proxies=self.proxies)
        # 获取收藏夹名数组和地址名数组
        re_mine_url = re.compile(r'<a href="(/collection/\d+?)"')
        list_mine_url = re.findall(re_mine_url, r.content)
        re_mine_name = re.compile(r'\d"\s>(.*?)</a>')
        list_mine_name = re.findall(re_mine_name, r.content)
        #print '收藏夹名称：', list_mine_name
        # for循环遍历数组
        for i in range(len(list_mine_url)):
            list_mine_url[i] = 'https://www.zhihu.com' + list_mine_url[i]
        #print '收藏夹地址：', list_mine_url
        conn = mysql.connector.connect(user='root', password='123456', database='test')
        cursor = conn.cursor()
        for i in range(len(list_mine_url)):
            page = 0
            sql = 'create table %s (id integer(10) primary key auto_increment, name varchar(100), address varchar(100))' % list_mine_name[i].decode("UTF-8")
            print sql
            cursor.execute(sql)
            conn.commit()
            while 1:
                page += 1
                col_url = list_mine_url[i]
                col_url = col_url + '?page=' + str(page)
                print '正在抓取：', col_url
                r = self.s.get(col_url, headers=self.headers, proxies=self.proxies)
                re_col_url = re.compile(r'href="(/question/\d*?)">.+?</a></h2>')
                list_col_url = re.findall(re_col_url, r.content)
                re_col_name = re.compile(r'\d">(.+?)</a></h2>')
                list_col_name = re.findall(re_col_name, r.content)
                if list_col_name:
                    #print '问题名称', list_col_name
                    # for循环遍历数组
                    for j in range(len(list_col_url)):
                        list_col_url[j] = 'https://www.zhihu.com' + list_col_url[j]
                    #print '问题地址：', list_col_url
                    for j in range(len(list_col_url)):
                        sql = 'insert into %s (name, address) values ("%s", "%s")' % (list_mine_name[i].decode("UTF-8"), list_col_name[j].decode("UTF-8"), list_col_url[j])
                        cursor.execute(sql)
                        conn.commit()
                else:
                    print '该收藏夹已无更多问题'
                    break
        cursor.close()

spider = Spider()
spider.get_collections()
print '爬虫执行完毕，请检查数据库'
