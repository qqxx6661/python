#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: test.py
@time: 2018/8/10 14:06
"""
import refrom collections import CounterfilePath = './sound.txt'def getCountWords(file):	"统计输入文件内容中单词的个数"	pattern = "[A-Za-z]+|\$?\d+%?$"	with open(file) as f:	 r = re.findall(pattern,f.read())	 print r	 print '*'*20	 return Counter(r).most_common()if __name__ == '__main__':	print getCountWords(filePath)