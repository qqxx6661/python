#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/8/30 18:57
"""
import sys

def eat(list, K, times):
    temp_times = 0
    for value in list:
        # print('temp_times += ', temp_times)
        if value == K:  # 正好相等，应该一次吃完
            temp_times += 1
            continue
        temp_times += ((value // K) + 1)

    if temp_times <= times:
        # print('temp_times = ', temp_times)
        return True
    return False

def search(list, times):
    if not list:
        return 0
    left = sum(list) // times
    right = max(list)
    # print(left,right)

    result = sys.maxsize
    while left <= right:
        mid = left + (right - left) // 2
        # print('mid', mid)
        if eat(list, mid, times):
            if result > mid:
                result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
        

lines = sys.stdin.readline().strip()
maoliang = list(map(int, lines.split(' ')))
times = int(sys.stdin.readline().strip())
# print(maoliang, times)
print(search(maoliang, times))


