#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/10/10 20:02
"""
# coding=utf-8
import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    n = values[0]
    m = values[1]
    line = sys.stdin.readline().strip()
    result_list = list(map(int, line.split()))
    # print(result_list)
    for _ in range(m):
        flag = 0
        min_value_index = result_list.index(min(result_list))
        if min_value_index == 0:
            extra_value_index = 1
        elif min_value_index == n-1:
            extra_value_index = n-2
            flag = 1
        else:
            if result_list[min_value_index-1] <= result_list[min_value_index+1]:
                extra_value_index = min_value_index - 1
                flag = 1
            else:
                extra_value_index = min_value_index + 1
        temp_sum = result_list[extra_value_index] + result_list[min_value_index]
        # print('ready to delete index:', min_value_index, extra_value_index)
        if flag == 0:  # min_value_index < extra_value_index
            del_index = min_value_index
        else:
            del_index = extra_value_index

        result_list = result_list[:del_index] + [temp_sum] + result_list[del_index+2:]
        # result_list = result_list_temp
        # result_list.pop(del_index)
        # result_list.pop(del_index)
        # result_list.insert(del_index, temp_sum)
        # print(result_list)
    print(min(result_list))