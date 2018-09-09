# py2.7 oneline

import sys
for line in sys.stdin:
    a = line.split()
    print int(a[0]) + int(a[1])

# py2.7 multiline

#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = map(int, line.split())
        for v in values:
            ans += v
    print ans

# py3.5 oneline

#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

# py3.5 multiline

#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)


# python3 normal dp

#coding=utf-8
import sys
if __name__ == "__main__":
    str = sys.stdin.readline().strip()
    length = len(str)
    dp = [[0 for __ in range(length)] for __ in range(length)]
    for i in range(length):
        dp[i][i] = 1
    for i in range(length-1, -1, -1):
        for j in range(i+1, length):
            dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
            if str[i] == str[j]:
                dp[i][j] = dp[i][j] + dp[i+1][j-1] + 1
    # for dp_line in dp:
    #     print dp_line
    print(dp[0][length-1])