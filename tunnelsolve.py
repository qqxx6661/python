# -*- coding: utf-8 -*-
import sys


def get_distance(up_down, i):
    if up_down == 0:  # down
        flag = 1
        temp = i + 1
        distance = 0
        while flag:
            try:
                if down[i] <= down[temp] or down[i] > up[temp]:
                    flag = 0
                    continue
                temp += 1
                distance += 1
            except IndexError:
                flag = 0
                distance = 0
        return distance
    elif up_down == 1:  # up
        flag = 1
        temp = i + 1
        distance = 0
        while flag:
            try:
                if up[i] < down[temp] or up[i] >= up[temp]:
                    flag = 0
                    continue
                temp += 1
                distance += 1
            except IndexError:
                flag = 0
                distance = 0
        return distance
    else:
        print('wrong parameter')


def get_distance_west():
    temp_height = down[0] + 1
    max_distance_west = 0
    while temp_height <= up[0]:
        flag = 1
        temp = 1
        distance = 1
        while flag:
            try:
                if temp_height <= down[temp] or temp_height > up[temp]:
                    flag = 0
                    continue
                temp += 1
                distance += 1
            except IndexError:
                flag = 0
                distance = 0
        if max_distance_west < distance:
            max_distance_west = distance
        temp_height += 1
    return max_distance_west

with open('test1.txt', 'r') as f:
    number = 0
    for line in f.readlines():
        if (line != '\n') and number == 0:
            up = line.split()
            up = [int(x) for x in up if x]
            # print(up)
            number += 1
        elif (line != '\n') and number == 1:
            down = line.split()
            down = [int(x) for x in down if x]
            # print(down)
            number += 1
        elif (line != '\n') and number == 2:
            sys.exit('wrong number of lines')
        else:
            continue
if len(up) != len(down):
    sys.exit('different numbers in lines')
for x in range(len(up)):
    if down[x] >= up[x]:
        sys.exit('wrong input')

print('From the west, one can into the tunnel over a distance of %s' % get_distance_west())
max_distance = 0
for x in range(len(down)-1):
    temp_distance = get_distance(0, x)
    if temp_distance > max_distance:
        max_distance = temp_distance
    temp_distance = get_distance(1, x)
    if temp_distance > max_distance:
        max_distance = temp_distance
print('Inside the tunnel, one can into the tunnel over a maximum distance of %s' % max_distance)
