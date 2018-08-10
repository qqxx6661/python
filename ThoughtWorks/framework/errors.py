#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: errors.py
@time: 2018/7/27 20:48
"""


class ConnectivityException(Exception):
    def __init__(self, err='Maze format error.'):
        Exception.__init__(self, err)


class InvalidNumberException(Exception):
    def __init__(self, err='Invalid number format.'):
        Exception.__init__(self, err)


class IncorrectCommandException(Exception):
    def __init__(self, err='Incorrect command format.'):
        Exception.__init__(self, err)


class OutOfRangeNumberException(Exception):
    def __init__(self, err='Number out of range.'):
        Exception.__init__(self, err)
