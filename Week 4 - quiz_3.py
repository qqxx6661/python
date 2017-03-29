# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()


def size_of_largest_parallelogram():
    i = 0
    j = 3
    length = 4
    max_size = judge_parallelogram(i, j, length)
    return max_size


def judge_parallelogram(i, j, length):
    max_size_temp = 0
    for l in range(2, length+1):
        for ll in range(j - 1, j - 1 + length):
            print(grid[i + l - 1][ll], end='')
            if grid[i + l - 1][ll] == 0:
                max_size_temp2 = 0
                break
            max_size_temp2 = l * l
        print('--')
        if max_size_temp < max_size_temp2:
            max_size_temp = max_size_temp2
    return max_size_temp



try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
print(grid)
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides has a size of', size, end = '.\n')
else:
    print('There is no parallelogram with horizontal sides.')
            

