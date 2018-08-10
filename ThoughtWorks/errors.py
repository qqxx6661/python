#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: errors.py
@time: 2018/7/27 20:48
"""


class MazeException(Exception):
    def __init__(self, err='Maze error.'):
        Exception.__init__(self, err)


class ConnectivityException(MazeException):
    def __init__(self, err='Maze format error.'):
        MazeException.__init__(self, err)


class InvalidNumberException(MazeException):
    def __init__(self, err='Invalid number format.'):
        MazeException.__init__(self, err)


class IncorrectCommandException(MazeException):
    def __init__(self, err='Incorrect command format.'):
        MazeException.__init__(self, err)


class OutOfRangeNumberException(MazeException):
    def __init__(self, err='Number out of range.'):
        MazeException.__init__(self, err)
