#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/9/11 14:46
"""
import sys


def spiralOrder(matrix):
    if not matrix:
        return []
    up = 0
    left = 0
    down = len(matrix) - 1
    right = len(matrix[0]) - 1
    direct = 0  # 0: go right   1: go down  2: go left  3: go up
    res = []
    while True:
        if direct == 0:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
        if direct == 1:
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
        if direct == 2:
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
        if direct == 3:
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
        if up > down or left > right:
            return res
        direct = (direct + 1) % 4

if __name__ == "__main__":
    list_old = []
    # 读取第一行的n
    line_0 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    line_0 = list(map(int, line_0.split(',')))
    list_old.append(line_0)
    n = len(line_0)
    for i in range(n-1):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        line = list(map(int, line.split(',')))
        list_old.append(line)
    list_old[:] = map(list, zip(*list_old[::-1]))
    list_old[:] = map(list, zip(*list_old[::-1]))
    list_old[:] = map(list, zip(*list_old[::-1]))
    print(','.join(map(str,spiralOrder(list_old))))



