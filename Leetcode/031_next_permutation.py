"""
下一个排列:实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。

example:
输入：nums = [1,2,3]
输出：[1,3,2]
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :ptype nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i+1, len(nums) - 1
        while left< right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums


if __name__ == '__main__':
    nums = [1,2,3]
    s = Solution()
    print(print(s.nextPermutation(nums)))
