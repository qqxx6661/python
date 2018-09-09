#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/9/9 20:24
"""
import sys

def judge(dict, dian):
    full_list = [i for i in range(2, dian+1)]
    for i in range(len(dict[1])):
        full_list.remove(dict[1][i])
    # print(full_list)
    if not full_list:
        return "Yes"
    for i in range(len(full_list)):
        for value in dict[full_list[i]]:
            if value in full_list:
                return "No"
    return "Yes"


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        params = list(map(int, line.split()))


        dian = params[0]
        bian = params[1]
        if not dian or not bian:
            print("No")
        temp_dict = {}
        for i in range(dian):
            temp_dict[i+1] = []
        for i in range(bian):
            line_each = sys.stdin.readline().strip()
            line_each = list(map(int, line_each.split()))
            temp_dict[line_each[0]].append(line_each[1])
            temp_dict[line_each[1]].append(line_each[0])
        #print(temp_dict)
        print(judge(temp_dict, dian))
