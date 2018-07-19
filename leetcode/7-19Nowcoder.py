# coding=utf-8
import sys


def check(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
            continue
        else:
            temp = '('

        if stack:
            if stack[-1] == temp:
                stack.pop()
            else:
                return False
        else:
            return False

    if len(stack) != 0:
        return False
    return True


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    l = []
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        l.append(line)
    for i in range(n):
        print(l[i] + l[i])
        if check(l[i] + l[i]):

            ans += 1
        for j in range(i + 1, n):
            print(l[i] + l[j])
            print(l[j] + l[i])
            if check(l[i] + l[j]):
                ans += 1
            if check(l[j] + l[i]):
                ans += 1
    print(ans)

# #coding=utf-8
# import sys
# import math
# a = list(map(int, (sys.stdin.readline().strip().split(' '))))
# x = a[0]
# y = a[1]
# if y * math.log(x) > x * math.log(y):
#     print('>')
# elif y * math.log(x) < x * math.log(y):
#     print("<")
# else:
#     print('=')

# #coding=utf-8
# import sys
# import math
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     line = sys.stdin.readline().strip()
#     # 把每一行的数字分隔后转化成int列表
#     values = list(map(int, line.split()))
#     for v in values:
#         while v > 1:
#             v /= 2
#             print(v)
#             print(int(v) == v)
#             if int(v) == v:
#                 ans += 1
#             else:
#                 break
#
#     print(ans)