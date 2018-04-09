# #coding=utf-8
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = sys.stdin.readline().strip()
#     timestamp = sys.stdin.readline().strip().split(' ')
#     count = 0
#     print(timestamp)
#     for i in range(int(n)):
#         left = timestamp[i][0:2]
#         right = timestamp[i][3:5]
#         print(left, right)
#         if left == right or left == right[::-1]:
#             count += 1
#             continue
#         if left[0] == left[1] and right[0] == right[1]:
#             count += 1
#     print(count)


# #coding=utf-8
# import sys
# if __name__ == "__main__":
#     str = sys.stdin.readline().strip()
#     length = len(str)
#     dp = [[0 for __ in range(length)] for __ in range(length)]
#     for i in range(length):
#         dp[i][i] = 1
#     for i in range(length-1, -1, -1):
#         for j in range(i+1, length):
#             dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
#             if str[i] == str[j]:
#                 dp[i][j] = dp[i][j] + dp[i+1][j-1] + 1
#     # for dp_line in dp:
#     #     print dp_line
#     print dp[0][length-1]

# def lcs_dp(input_x, input_y):
#     # input_y as column, input_x as row
#     dp = [([0] * (len(input_y) + 1)) for i in range(len(input_x) + 1)]
#     for i in range(1, len(input_x) + 1):
#         for j in range(1, len(input_y) + 1):
#             if i == 0 or j == 0:  # 在边界上，自行+1
#                 dp[i][j] = 1
#             elif input_x[i - 1] == input_y[j - 1]:  # 不在边界上，相等就加一
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:  # 不相等
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#     for dp_line in dp:
#         print(dp_line)
#     return dp[-1][-1]
#
# if __name__ == "__main__":
#     a = 'abc'
#     print(a[::-1])
#     print(lcs_dp(a, a[::-1]))

# #coding=utf-8
# import sys
# import math
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = sys.stdin.readline().strip()
#     n = int(n)
#     for num in range(n):
#         line = sys.stdin.readline().strip()
#         line = int(line)
#         temp_i = 0
#         min_j = sys.maxint
#         x = int(math.sqrt(line))
#         for i in range(1, x+1):
#             print i, line % i
#             if line % i == 0:
#                 j = line / i
#                 if j % 2 == 0 and i % 2 == 1:
#                     print(i, j)
#                     if j < min_j:
#                         min_j = j
#                         temp_i = i
#                     continue
#                 if i % 2 == 0 and j % 2 == 1:
#                     print(j, i)
#                     if j < min_j:
#                         min_j = i
#                         temp_i = j
#         if min_j == sys.maxint:
#             print 'No'
#         else:
#             print str(temp_i) + ' ' + str(min_j)


# #coding=utf-8
# import sys
# import math
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = sys.stdin.readline().strip()
#     n = int(n)
#     for num in range(n):
#         line = sys.stdin.readline().strip()
#         line = int(line)
#         temp_i = 0
#         min_j = sys.maxint
#         x = int(math.sqrt(line))
#         for i in range(1, x+1):
#             if line % i == 0:
#                 j = line / i
#                 if (j % 2 == 0 and i % 2 == 1) or (i % 2 == 0 and j % 2 == 1):
#                     # print(i, j)
#                     if j < min_j:
#                         min_j = j
#                         temp_i = i
#         if min_j == sys.maxint:
#             print 'No'
#         elif min_j % 2 == 0:
#             print str(temp_i) + ' ' + str(min_j)
#         else:
#             print str(min_j) + ' ' + str(temp_i)

#coding=utf-8
import sys
import math
if __name__ == "__main__":
    # 读取第一行的n
    n = sys.stdin.readline().strip()
    n = int(n)
    for num in range(n):
        line = sys.stdin.readline().strip()
        line = int(line)
        temp_i = 0
        min_j = sys.maxsize
        x = int(math.sqrt(line))
        for i in range(1, x+1):
            if line % i == 0:
                j = line / i
                if j % 2 == 0 and i % 2 == 1:
                    # print(i, j)
                    if j < min_j:
                        min_j = int(j)
                        temp_i = int(i)
                    continue
                if i % 2 == 0 and j % 2 == 1:
                    # print(j, i)
                    if j < min_j:
                        min_j = int(i)
                        temp_i = int(j)
        if min_j == sys.maxsize:
            print('No')
        else:
            print(str(temp_i) + ' ' + str(min_j))