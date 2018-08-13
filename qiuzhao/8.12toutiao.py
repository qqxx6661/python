# 1

from queue import Queue
import sys


def readline():
    return sys.stdin.readline().strip()


_ = readline()
m, n = map(int, _.split(','))


def get_line():
    _ = readline()
    return list(map(int, _.split(',')))


seat_map = [get_line() for i in range(m)]
flag = [[0 for j in range(n)] for i in range(m)]


def bfs(i, j):
    num = 0
    sq = [(i, j)]

    def check_put(i, j):
        if i >= m or i < 0 or j >= n or j < 0 or flag[i][j] == 1 or seat_map[i][j] == 0:
            return
        flag[i][j] = 1
        sq.append((i, j))

    flag[i][j] = 1
    while len(sq) > 0:
        _i, _j = sq[0]
        sq = sq[1:]
        num += 1
        check_put(_i - 1, _j - 1)
        check_put(_i - 1, _j)
        check_put(_i - 1, _j + 1)
        check_put(_i, _j - 1)
        check_put(_i, _j + 1)
        check_put(_i + 1, _j - 1)
        check_put(_i + 1, _j)
        check_put(_i + 1, _j + 1)
    return num


p = 0
q = 0
for i in range(m):
    for j in range(n):
        if flag[i][j] == 0 and seat_map[i][j] == 1:
            _q = bfs(i, j)
            p += 1
            if q < _q:
                q = _q

print(str(p) + ',' + str(q))

# 2

#coding=utf8
import sys

def merge(intervals):
    output = list()
    if len(intervals) == 0:
        return output
    intervals.sort(key=lambda x: x[0])
    output.append(intervals[0])
    for i in range(1, len(intervals)):
        if output[-1][1] < intervals[i][0]:
            output.append(intervals[i])
        else:
            output[-1][1] = max(intervals[i][1], output[-1][1])
    return output

if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    n = int(line1)
    intervals = list()
    for i in range(n):
        line = sys.stdin.readline().strip()
        items = line.split(';')
        for item in items:
            s, e = item.split(',')
            intervals.append([int(s), int(e)])
    output = merge(intervals)
    output_str = [str(t[0]) + ',' + str(t[1]) for t in output]
    print ';'.join(output_str)

# 3

import sys


def maxNum(n):

    card = []
    for i in range(n):
        line = sys.stdin.readline()
        card.append(list(map(int, line.split())))

    sum_x = 0
    sum_y = 0
    for i in range(n):
        sum_x += card[i][0]
        sum_y += card[i][1]

    if sum_x % 2 == 0:
        max_team = sum_y
    else:
        min_y = card[0][1]
        for i in range(n):
            if card[i][1] < min_y and card[i][0] % 2 != 0:
                min_y = card[i][1]
        max_team = sum_y - min_y
    return max_team


line = sys.stdin.readline()
n = int(line)
print(maxNum(n))

# 4

c++

# include <iostream>
# include <vector>


using
namespace
std;

int
findmax(vector < long > & a, int
begin, int
end)
{
    int
max = a[begin];
while (begin <= end)
    {
    if (max < a[begin])
    max = a[begin];
    begin + +;
    }
    return max;
}

int
findmin(vector < long > & b, int
begin, int
end)
{
int
min = b[begin];
while (begin <= end)
    {
    if (min > b[begin])
    min = b[begin];
    begin + +;
    }
    return min;
    }


    int
    main()
    {
    int
    n;
    cin >> n;

    vector < long > a;
    vector < long > b;

    int
    count = 0;

    long
    num = 0;
    for (int i = 0; i < 2 * n; i++)
    {
        cin >> num;
    if (i < n)
    a.push_back(num);
    else
    b.push_back(num);
    }

    for (int i = 0; i < n; i++)
    {
    for (int j = i; j < n; j++)
    {
    int max = findmax(a, i, j);
    int min = findmin(b, i, j);
    if (max < min)
    count++;
    }
    }

    cout << count << endl;
    return 0;
    }

# 5