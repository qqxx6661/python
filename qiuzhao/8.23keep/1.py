# coding=utf-8
import sys


def merge(intervals):
    result = []
    if not intervals:
        return result
    intervals.sort(key=lambda x: x[0])  # 按照左区间排序（请看下方总结）
    result.append(intervals[0])  # 先将第一个加入区间
    for interval in intervals[1:]:
        prev = result[-1]  # 数组最后一个
        if prev[1] > interval[0]:  # 如果有交叉，将前一个区间的end变为他们两的最大值
            return False
        else:
            result.append(interval)
    return True


if __name__ == "__main__":
    values = []
    lines = sys.stdin.readline().strip().split(' ')
    for line in lines:
        values.append(list(map(int, line.split(','))))
    # print(values)
    print(merge(values))


