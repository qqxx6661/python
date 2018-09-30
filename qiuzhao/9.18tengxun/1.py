#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/9/18 20:50
"""

# coding=utf-8
import sys


def manh(a, b):
    # print(a,b,sum(map(lambda i, j: abs(i - j), a, b)))
    return sum(map(lambda i, j: abs(i - j), a, b))


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    dian_count = values[0]
    chufa_count = values[1]
    dian_list = []
    for i in range(dian_count):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        dian_values = list(map(int, line.split()))
        dian_list.append([dian_values[0], dian_values[1]])
    # print(dian_list)
    for i in range(chufa_count):
        result = 0
        line = sys.stdin.readline().strip()
        chufa_values = list(map(int, line.split()))
        for j in range(dian_count):
            result += manh([chufa_values[0], chufa_values[1]], dian_list[j])
        print(result)
