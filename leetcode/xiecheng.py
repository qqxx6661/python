import sys
import os
import re

def calculate_length(result_list, max_length):
    if not result_list:
        return max_length
    for i in range(len(result_list)):
        while True:
            for j in range(i+1, len(result_list)):
                if result_list[j]


def calculate(M, strs):
    result_list = []
    for each_str in strs:
        for i in range(0, len(each_str), 2):
            j = i + 2
            while j <= len(each_str) - 1:
                print re.findall(r"\d+\.?\d*", each_str[i:j])
                result_list.append([each_str[i], each_str[j], sum(map(int,re.findall(r"\d+\.?\d*", each_str[i:j])))])
                j += 2

    return calculate_length(result_list, 0)
if __name__ == "__main__":
    M = 4
    strs = ["A2B3D", "A4C2E", "A5D", "C3B"]
    res = calculate(M, strs)
    print res