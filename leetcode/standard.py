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
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

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


