#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/9/21 16:14
"""
import sys
if __name__ == "__main__":
    # 读取第一行的n
    num = int(sys.stdin.readline().strip())
    result = ''
    while True:
        if num == 1:
            result += "2"
            print(result[::-1])
            break
        if num == 2:
            result += "3"
            print(result[::-1])
            break
        # print(num)
        if num % 2 == 1:
            num = (num-1)//2
            result += "2"
        else:
            num = (num-2)//2
            result += "3"
