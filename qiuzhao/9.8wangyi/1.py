#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/9/8 16:20
"""
# coding=utf-8
import sys


def solver(N, M):
    l = [[1 for _ in range(N)] for _ in range(M)]

    for i in range(M):
        print(l[i])

    def reverse(x, y):
        if l[x][y] == '1':
            l[x][y] = '0'
        else:
            l[x][y] = '1'
        if l[x - 1][y - 1] == '1':
            l[x - 1][y - 1] = '0'
        else:
            l[x - 1][y - 1] = '1'
        if l[x - 1][y] == '1':
            l[x - 1][y] = '0'
        else:
            l[x - 1][y] = '1'
        if l[x - 1][y + 1] == '1':
            l[x - 1][y + 1] = '0'
        else:
            l[x - 1][y + 1] = '1'
        if l[x][y - 1] == '1':
            l[x][y - 1] = '0'
        else:
            l[x][y - 1] = '1'
        if l[x][y + 1] == '1':
            l[x][y + 1] = '0'
        else:
            l[x][y + 1] = '1'
        if l[x + 1][y - 1] == '1':
            l[x + 1][y - 1] = '0'
        else:
            l[x + 1][y - 1] = '1'
        if l[x + 1][y] == '1':
            l[x + 1][y] = '0'
        else:
            l[x + 1][y + 1] = '1'
        if l[x + 1][y + 1] == '1':
            l[x + 1][y + 1] = '0'
        else:
            l[x + 1][y + 1] = '1'

    for i in range(N):
        for j in range(M):
            reverse(i, j)

    for i in range(M):
        print(l[i])


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    point_list = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        solver(values[0], values[1])
