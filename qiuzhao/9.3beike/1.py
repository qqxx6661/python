#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/9/3 19:49
"""
#coding=utf-8
import random
import sys
import queue


if __name__ == "__main__":
    def f(temp, MM, step, result):
        print(temp, MM, step, result)
        if temp > MM: return
        if temp < 2: return
        if temp == MM:
            if result > step:
                result = step
        f(temp - 1, MM, step + 1, result)
        f(temp * 2, MM, step + 1, result)

    # 读取第一行的n
    l = sys.stdin.readline().strip().split(' ')
    N = int(l[0])
    M = int(l[1])
    result = sys.maxsize
    f(N, M, 0, result)

    print(result)


