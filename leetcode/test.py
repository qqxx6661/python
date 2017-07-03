# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        index_i = 0
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y == x:  # 有输入[3,3]，所以需要找出两个3的位置，根据题目规定，不可能出现三个三
                if nums.count(x) == 2:
                    for num_same in nums:
                        if x == num_same:
                            result.append(index_i)
                        index_i += 1
                    return result
            if y in nums:
                result.append(i)
                result.append(nums.index(y))
                return result

a = [1, 3, 3]
s = Solution()
print(s.twoSum(a, 6))
