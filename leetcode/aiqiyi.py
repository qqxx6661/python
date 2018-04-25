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
if __name__ == "__main__":
    # 读取第一行的n
    a = list(sys.stdin.readline().strip().split(' '))
    n = int(a[0])
    m = int(a[1])
    m_dict = {}
    for i in range(n):
        m_dict[i] = list(map(int, (sys.stdin.readline().strip().split(' '))))
    count = digui(0, m, 0, n)
    print count
