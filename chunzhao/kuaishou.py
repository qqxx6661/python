#coding=utf-8
import sys


def myPow(m, n):
    if n == 0:
        return 1
    elif n < 0:
        m = 1 / m
        n = -n
    ans = 1
    while n > 0:
        if n & 1:
            ans *= m
        m *= m
        n >>= 1
    return ans

if __name__ == "__main__":
    nums = list(map(long, (sys.stdin.readline().strip().split(' '))))
    x = nums[0]
    y = nums[1]
    N = nums[2]
    print long(myPow(x, y)) % N

# #coding=utf-8
# import sys
# def binary_search(find, list1) :
#     low = 0
#     high = len(list1) - 1
#     while low <= high:
#         mid = low + (high - low) / 2
#         if list1[mid] == find:
#             return mid
#         elif list1[mid] > find:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return low
#
#
#
# if __name__ == "__main__":
#     nums = list(map(int, (sys.stdin.readline().strip().split(' '))))
#     x = int(sys.stdin.readline().strip())
#     print binary_search(x, nums)