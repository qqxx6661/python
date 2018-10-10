#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 3.py
@time: 2018/10/10 20:54
"""
# coding:utf-8
# !/bin/python

import sys


def is_pop_order(pushV, popV):
    if len(pushV) == 0:
        return False
    stack = []
    j = 0
    for i in range(len(pushV)):
        stack.append(pushV[i])
        while j < len(popV) and stack[-1] == popV[j]:
            stack.pop()
            j += 1
    if len(stack) == 0:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    n = 4
    l_pop = []
    for i in range(n):
        # 读取每一行
        line = int(sys.stdin.readline().strip())
        l_pop.append(line)
    print(is_pop_order([1, 2, 3, 4], l_pop))
