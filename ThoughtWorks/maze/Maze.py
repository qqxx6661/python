#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: maze.py
@time: 2018/7/27 22:37
"""
from errors import ConnectivityException, OutOfRangeNumberException, IncorrectCommandException


class Maze:
    """迷宫类
    len_x:行
    len_y:列
    lines:连通性描述
    render_grid:渲染网格
    """

    def __init__(self, size, lines):
        self.len_x, self.len_y = size
        self.lines = lines
        self.render_grid = []

    def render(self):
        """生成渲染网格流程：
        1.生成全'[w]'填充的二维数组，大小为[2x+1][2y+1]
        2.在渲染网格中将点坐标填充为'[r]'
        3.将联通的两点之间填充为'[r]'
        :return: 渲染网格
        """
        self.render_grid = [["[W]" for _ in range(2 * self.len_y + 1)] for _ in range(2 * self.len_x + 1)]
        for x in range(self.len_x):
            for y in range(self.len_y):
                self.render_grid[2 * x + 1][2 * y + 1] = "[R]"
        for line in self.lines:
            x_1, y_1, x_2, y_2 = line[0][0], line[0][1], line[1][0], line[1][1]
            if x_1 >= self.len_x or x_2 >= self.len_x or y_1 >= self.len_y or y_2 >= self.len_y:
                raise OutOfRangeNumberException
            if x_1 == x_2 and y_1 != y_2:
                if y_1 < y_2:
                    self.render_grid[2 * x_1 + 1][2 * y_1 + 2] = "[R]"
                if y_1 > y_2:
                    self.render_grid[2 * x_1 + 1][2 * y_2 + 2] = "[R]"
                continue
            if x_1 != x_2 and y_1 == y_2:
                if x_1 < x_2:
                    self.render_grid[2 * x_1 + 2][2 * y_1 + 1] = "[R]"
                if x_1 > x_2:
                    self.render_grid[2 * x_2 + 2][2 * y_1 + 1] = "[R]"
                continue
            raise ConnectivityException
        return self.render_grid
