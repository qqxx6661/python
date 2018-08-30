#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 1.py
@time: 2018/8/30 18:57
"""
import sys

def maxProfit(prices):
    if not prices:
        return 0
    dp = [0 for __ in range(len(prices))]
    minPrice = prices[0]
    for i in range(1, len(prices)):
        dp[i] = max(dp[i - 1], prices[i] - minPrice)
        if (minPrice > prices[i]):
            minPrice = prices[i]
    return dp[-1]

lines = sys.stdin.readline().strip()
prices = list(map(int, lines.split(' ')))
print(maxProfit(prices))


