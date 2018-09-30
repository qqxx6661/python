#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: 3.py
@time: 2018/9/17 20:59
"""
import sys

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    size = len(coins)
    dp = [1] + [0] * amount
    for i in range(size):
        for j in range(amount):
            if j + coins[i] <= amount:
                dp[j + coins[i]] += dp[j]
    return dp[-1]



if __name__ == "__main__":
    a = [1, 5, 10, 20, 50]
    value = int(sys.stdin.readline().strip())
    print(coinChange(a,value))
