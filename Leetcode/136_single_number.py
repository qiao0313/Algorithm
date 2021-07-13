"""
只出现一次的数字: 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

example:
输入: [2,2,1]
输出: 1
"""

from functools import reduce

# 异或
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    nums = [2,2,1]
    s = Solution()
    print(s.singleNumber(nums))