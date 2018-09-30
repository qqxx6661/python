#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 2.py
@time: 2018/9/26 16:37
"""
import sys
def count_people(n):
    age = 4
    if n == 1:
        return age

    for i in range(2, n+1):
        age += i-1
    return age


if __name__ == "__main__":
    print(count_people(5))