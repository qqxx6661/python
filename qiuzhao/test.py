#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: test.py
@time: 2018/8/10 14:06
"""
def triangles():
    N=[1]
    while True:
        yield N
        N.append(0)
        print(N)

        N=[N[i-1] + N[i] for i in range(len(N))]

n=0
for t in triangles():
    print(t)
    n=n+1
    if n == 10:
        break
