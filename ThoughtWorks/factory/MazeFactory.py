#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: mazefactory.py
@time: 2018/7/27 22:31
"""
from errors import InvalidNumberException, IncorrectCommandException
from maze import Maze


class MazeFactory(object):
    """迷宫工厂
    静态工厂，不需要实例化
    """

    @staticmethod
    def str2list(string, symbol):
        try:
            param_list = list(map(int, string.split(symbol)))
        except ValueError:
            raise InvalidNumberException
        return param_list

    @staticmethod
    def create(maze_info):
        """处理迷宫描述信息流程：
        1.将网格大小转为int型数组
        2.将连通性定义拆分为string型数组[['0', '1'], ['0', '2']]
        3.进一步拆分为int型数组[[0, 1], [0, 2]]
        :param maze_info: 迷宫描述信息
        :return: 创建迷宫实例对象
        """
        try:
            size = MazeFactory.str2list(maze_info[0], ' ')
            lines = [line.split() for line in maze_info[1].split(';')]
            for i, line in enumerate(lines):
                if len(line) != 2:
                    raise IncorrectCommandException
                lines[i][0] = MazeFactory.str2list(line[0], ',')
                lines[i][1] = MazeFactory.str2list(line[1], ',')
            if len(size) != 2:
                raise IncorrectCommandException
            return Maze(size, lines)
        except (IndexError, AttributeError):
            raise IncorrectCommandException
