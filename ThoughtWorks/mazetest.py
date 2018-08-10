#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: mazetest.py
@time: 2018/7/27 17:55
"""

from errors import MazeException
from factory import MazeFactory


def stdout(func):
    """标准化输出装饰器
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        print('-----Start test-----')
        print('Test case:', args[0])
        print('Output:')
        func(*args, **kwargs)
    return wrapper


class MazeTest:

    @staticmethod
    @stdout
    def test(case):
        try:
            maze = MazeFactory.create(case)
            maze_text = maze.render()
            for line in maze_text:
                print(line)
        except MazeException as e:
            print(e)


if __name__ == "__main__":

    test_cases = [
        # 正确
        ["3 3", "0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"],
        # 存在字母x，无效的数字，应返回Invalid number format.
        ["3 x", "0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"],
        # 存在[0,3 0,2]，数字超出预定范围，应返回Number out of range.
        ["3 3", "0,3 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"],
        # 缺少连通性定义，有格式错误，应返回Incorrect command format.
        ["3 3"],
        # 存在[0,1 1,2]，有连通性错误，应返回Maze format error.
        ["3 3", "0,1 1,2;0,1 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"]
    ]

    for test_case in test_cases:
        MazeTest.test(test_case)
