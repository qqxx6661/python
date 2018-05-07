# #coding=utf-8
# import sys
# import collections
# def Permutation(nums):
#     if nums == '':
#         return []
#     nums = list(nums)
#     nums.sort()
#     used = {x: set() for x in range(len(nums) + 1)}
#     count = collections.Counter(nums)
#     key = collections.defaultdict(int)
#     an = []
#
#     def dfs(cur, idx):
#         used[idx].add(cur)
#         if idx == len(nums):
#             an.append(cur)
#             return
#
#         for x in nums:
#             if key[x] < count[x]:
#                 key[x] += 1
#                 if cur + (x,) not in used[idx + 1]:
#                     dfs(cur + (x,),idx + 1)
#                 key[x] -= 1
#     dfs((),0)
#     return [''.join(x) for x in an]
#
# if __name__ == "__main__":
#     nums = sys.stdin.readline().strip()
#     print Permutation(nums)

# # coding=utf-8
# import sys
# def candy(ratings):
#     n = len(ratings)
#     result = [1 for __ in range(n)]
#     for i in range(1, n):
#         if ratings[i-1] < ratings[i]:
#             result[i] = result[i-1] + 1
#     for j in range(n-2, -1, -1):
#         if ratings[j] > ratings[j+1]:
#             result[j] = max(result[j], result[j+1] + 1)
#     return sum(result)
#
# if __name__ == "__main__":
#     nums = list(map(int, (sys.stdin.readline().strip().split(','))))
#     print candy(nums)

l = ['abc','aaa']
print(str(l).replace('\'',''))