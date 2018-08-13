#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 8.11wangyi.py
@time: 2018/8/11 14:28
"""
# coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    str1 = sys.stdin.readline().strip().split()
    了 = int(str1[0])
    xings = list(map(int, str3.split()))
    k = int(str1[1])
    scores = list(map(int, str2.split()))

    #print(scores)
    #print(xings)
    #print(scores_cut)
    #print(scores_cut_1)
    for i, v in enumerate(xings):
        if v == 1:
            scores_cut[i] = 0
        if v == 0:
            scores_cut_1[i] = 0
    max_result = 0
    index_result = 0
    #print('------')
    #print(scores_cut)
    #print(scores_cut_1)
    for i in range(n):
        max_temp = sum(scores_cut[i:i+k])
        if max_temp > max_result:
            max_result = max_temp
            index_result = i
    print(max_result + sum(scores_cut_1))


