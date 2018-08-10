# #coding=utf-8
# import sys
# if __name__ == "__main__":
#     nums = list(map(int, (sys.stdin.readline().strip().split(' '))))
#     nums.sort()
#     a = nums[0]
#     b = nums[1]
#     c = nums[2]
#     count = c - b
#     if a != b:
#         if (c - (a + (c - b))) % 2 == 0:
#             count += (c - (a + (c - b))) / 2
#         else:
#             count += (c - (a + (c - b))) / 2
#             count += 2
#     print count


# #coding=utf-8
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     nums = list(map(int, (sys.stdin.readline().strip().split(' '))))
#     times = int(sys.stdin.readline().strip())
#     cut_loc = list(map(int, (sys.stdin.readline().strip().split(' '))))
#     for i in range(times):
#         left = nums[:cut_loc[i]]
#         right = nums[cut_loc[i]:]
#         temp = []
#         while left and right:
#             temp.append(left.pop())
#             temp.append(right.pop())
#         if left:
#             left.reverse()
#             temp += left
#         else:
#             right.reverse()
#             temp += right
#         temp.reverse()
#         nums = temp
#     print ' '.join(str(i) for i in nums)

#coding=utf-8
import sys


def sortColors(nums):
    left = mid = 0
    right = len(nums) - 1
    while mid <= right:
        if nums[mid] == 0:
            nums[mid], nums[left] = nums[left], nums[mid]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
if __name__ == "__main__":
    # 读取第一行的n
    ary = sys.stdin.readline().strip()
    ary = list(ary)
    for i in range(len(ary)):
        # ary[i] = ary[i][1:-1]
        if ary[i] == 'R':
            ary[i] = 0
        elif ary[i] == 'G':
            ary[i] = 1
        else:
            ary[i] = 2
    sortColors(ary)
    for i in range(len(ary)):
        if ary[i] == 0:
            ary[i] = 'R'
        elif ary[i] == 1:
            ary[i] = 'G'
        else:
            ary[i] = 'B'
    print ''.join(ary)
