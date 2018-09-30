#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 2.py
@time: 2018/9/15 22:49
"""
import sys
from functools import reduce


def ip_into_int(ip):
    # 先把 192.168.1.13 变成16进制的 c0.a8.01.0d ，再去了“.”后转成10进制的 3232235789 即可。
    # (((((192 * 256) + 168) * 256) + 1) * 256) + 13
    return reduce(lambda x,y:(x<<8)+y,map(int,ip.split('.')))

def is_internal_ip(ip):
    ip = ip_into_int(ip)
    net_a = ip_into_int('10.255.255.255') >> 24
    net_b = ip_into_int('172.31.255.255') >> 20
    net_c = ip_into_int('192.168.255.255') >> 16
    return ip >> 24 == net_a or ip >>20 == net_b or ip >> 16 == net_c



if __name__ == '__main__':
    ip = sys.stdin.readline().strip()
    if is_internal_ip(ip):
        print('true')
    else:
        print('false')