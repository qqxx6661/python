#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/9/7 19:51
"""
import sys
def maxSubArray(nums, target):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 'false'
    if target == nums[0]:
        return 'true'
    dp = [nums[0] for i in range(len(nums))]
    max_result = nums[0]  # 最开始的是nums[0]，后面如果是负数肯定更小，如果是整数肯定变大
    flag_10 = 0
    flag_500 = 0
    for i in range(1, len(nums)):
        if nums[i] + nums[i-1] > 10.0:
            flag_10 = 1
        if dp[i-1] < 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1] + nums[i]
        if max_result < dp[i]:
            max_result = dp[i]
            print(max_result)
            if max_result == target:
                flag_500 = 1
    print(flag_10, flag_500)
    if flag_10 and flag_500:

        return 'true'
    return 'false'


if __name__ == "__main__":
    # 读取第一行的n
    l = list(map(int,sys.stdin.readline().strip().split(',')))
    k = int(sys.stdin.readline().strip())
    print(maxSubArray(l,k))


