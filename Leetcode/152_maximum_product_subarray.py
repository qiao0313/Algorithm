"""
乘积最大子数组: 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

example:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
"""


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxValue = - 9999
        imax, imin = 1,  1
        for i in range(len(nums)):
            if nums[i] < 0:
                tmp = imax
                imax = imin
                imin = tmp
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])

            maxValue = max(maxValue, imax)

        return maxValue


if __name__ == '__main__':
    nums = [2,3,-2,4]
    s = Solution()
    print(s.maxProduct(nums))