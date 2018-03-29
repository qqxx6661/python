#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = sys.stdin.readline().strip()
    lr_str = sys.stdin.readline().strip()
    diff = lr_str.count("L") - lr_str.count("R")
    if diff < 0:
        diff = abs(diff)
    face = diff % 4
    if face == 1:
        print 'E'
    elif face == 2:
        print 'S'
    elif face == 3:
        print 'W'
    else:
        print 'N'


# #coding=utf-8
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     s = sys.stdin.readline().strip()
#     s = s.split(' ')
#     n = int(s[0])
#     k = int(s[1])
#     result = 0
#     temp_result = 0
#     if k == 0:
#         result = 2 * n + result
#     for i in range(1, n+1):
#         for j in range(1, i):
#             print(i, j, i % j, j % i)
#             if i % j >= k:
#                 temp_result += 1
#             if j % i >= k:
#                 temp_result += 1
#
#     print temp_result
#
#     print result + temp_result


# # -*- coding: utf-8 -*-
# # n为物品数量
# # c为背包重量
# # w为每个物品重量
# # v为每个物品价值
# def bag(n, c, w, v):
#     res = [[-1 for j in range(c + 1)] for i in range(n + 1)]
#     for j in range(c + 1):
#         res[0][j] = 0
#     for i in range(1, n + 1):
#         for j in range(1, c + 1):
#             res[i][j] = res[i - 1][j]
#             if j >= w[i - 1] and res[i][j] < res[i - 1][j - w[i - 1]] + v[i - 1]:
#                 res[i][j] = res[i - 1][j - w[i - 1]] + v[i - 1]
#     for line in res:
#         print(line)
#     return res
#
#
#
# if __name__ == '__main__':
#     n = 3
#     c = 10
#     w = [1, 2, 4]
#     v = [7, 3, 10]
#     res = bag(n, c, w, v)