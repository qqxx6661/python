#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/9/28 19:23
"""
import sys


def cni(n, i):
    result = 1
    for j in range(1, i + 1):
        result = result * (n - i + j) // j
    return result


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    count = 1
    m = (n + 1) // 2
    for i in range(1, m + 1):
        # combins = [c for c in combinations(range(n), n - i + 1)]
        combins = cni(n - i + 1, i)
        count += combins
    print(count)
