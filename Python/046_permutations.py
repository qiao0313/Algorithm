"""
全排列: 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

example:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            prefix = nums[i]
            rest = nums[:i] + nums[i+1:]
            for j in self.permute(rest):
                res.append([prefix]+j)

        return res


if __name__ == '__main__':
    nums = [1 ,2, 3]
    s = Solution()
    print(s.permute(nums))