"""
全排列 II: 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

example:
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""


class Solution:
    def permuteUnique(self, nums):
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
            for j in self.permuteUnique(rest):
                if [prefix]+j not in res:
                    res.append([prefix]+j)
        return res


if __name__ == '__main__':
    nums = [1, 1, 2]
    s = Solution()
    print(s.permuteUnique(nums))