# coding=utf-8
import sys

# test = [(1, 5), (2, 6), (3, 7)]

test = []
n = int(sys.stdin.readline().strip(''))
for i in range(n):
    line = list(map(int,sys.stdin.readline().strip().split(' ')))
    test.append((line[0], line[1]))



res = 0
flag = list()
num = len(test)
for i in range(num):
    tmp = test.pop(0)
    tmp_test = test[:]
    tmp_test = sorted(tmp_test, key=lambda x: x[1], reverse=False)
    right = True
    for j in range(num-2):
        if tmp_test[j][1] > tmp_test[j+1][0]:
            right = False
            break
    if right:
        res +=1
        flag.append(i+1)
    test.append(tmp)
if res == 0:
    print(res)
else:
    print(res)
    print(' '.join(['1','2','3']))
    print(' '.join([str(i) for i in flag]))

# res = 0
# flag = list()
# num = len(test)
# for i in range(num):
#     tmp = test.pop(0)
#     test = sorted(test, key=lambda x: x[1], reverse=False)
#     right = True
#     for j in range(num - 2):
#         if test[j][1] > test[j + 1][0]:
#             right = False
#             break
#     if right:
#         res += 1
#         flag.append(i + 1)
#     test.append(tmp)
# if res == 0:
#     print(res)
# else:
#     print(res, flag)
