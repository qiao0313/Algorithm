"""
缺失的第一个正数:给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

example:
输入：nums = [1,2,0]
输出：3
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        old_missing, missing = 0, 1
        while old_missing != missing:
            old_missing = missing
            for i in range(len(nums)):
                if nums[i] == missing:
                    missing += 1
        return missing


if __name__ == '__main__':
    nums = [1,2,0]
    s = Solution()
    print(s.firstMissingPositive(nums))