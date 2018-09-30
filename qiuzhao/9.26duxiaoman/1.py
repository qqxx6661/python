#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/9/26 16:19
"""
import sys
if __name__ == "__main__":
    # 读取第一行的n
    num = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    count = 0
    temp_dict = {}
    result = []
    for i in range(num-1):
        count = 0
        temp_dict = {}
        left = values[:i+1]
        right = values[i+1:]
        print(left,right)
        for v_left in left:
            if v_left not in temp_dict:
                temp_dict[v_left] = 0
                for v_right in right:
                    if v_left != v_right:
                        count += 1
                        temp_dict[v_left] += 1
            else:
                print('jump')
                count += temp_dict[v_left]
        result.append(count)
    print(' '.join(str(i) for i in result))