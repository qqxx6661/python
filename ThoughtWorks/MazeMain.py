#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: MazeMain.py
@time: 2018/7/27 17:55
"""
import sys

from ThoughtWorks.framework.errors import OutOfRangeNumberException
from ThoughtWorks.framework.errors import IncorrectCommandException
from ThoughtWorks.framework.errors import InvalidNumberException
from ThoughtWorks.framework.errors import ConnectivityException
from ThoughtWorks.factory.MazeFactory import MazeFactory


def stdout(func):
    def wrapper(*args, **kwargs):
        print('-----Start test-----')
        print('Test case:', args[0])
        print('Output:')
        func(*args, **kwargs)

    return wrapper


@stdout
def test(test_case):
    try:
        maze = MazeFactory.create(test_case)
        maze_text = maze.render()
        for line in maze_text:
            print(line)
    except (ConnectivityException, InvalidNumberException, IncorrectCommandException,
            OutOfRangeNumberException) as e:
        print(e)
    except:
        print("Unexpected error:", sys.exc_info()[0])


if __name__ == "__main__":

    test_cases = [
        # 正确
        ["3 3", "0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"],
        # 存在字母x，无效的数字，应返回Invalid number format.
        ["x 3", "0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"],
        # 存在[0,3 0,2]，数字超出预定范围，应返回Number out of range.
        ["3 3", "0,3 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"],
        # 缺少连通性定义，存在格式错误，应返回Incorrect command format.
        ["3 3"],
        # 存在[0,1 1,2]，违反连通约束，应返回Maze format error.
        ["3 3", "0,1 1,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"]]

    for test_case in test_cases:
        test(test_case)
