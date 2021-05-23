"""
只出现一次的数字 II: 给你一个整数数组 nums，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

example:
输入：nums = [2,2,3,2]
输出：3
"""

# 数字电路设计
class Solution:
    def singleNumber(self, nums):
        """
        :type mums: List
        :rtype: int
        """
        a = b =0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b


if __name__ == '__main__':
    nums = [2,2,3,2]
    s = Solution()
    print(s.singleNumber(nums))