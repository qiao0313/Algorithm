"""
和为 S 的两个数字: 在有序数组中找出两个数，使得和为给定的数 S。如果有多对数字的和等于 S，输出两个数的乘积最小的。

解题思路：
使用双指针，一个指针指向元素较小的值，一个指针指向元素较大的值。指向较小元素的指针从头向尾遍历，指向较大元素的指针从尾向头遍历。
    如果两个指针指向元素的和 sum == target，那么这两个元素即为所求。
    如果 sum > target，移动较大的元素，使 sum 变小一些；
    如果 sum < target，移动较小的元素，使 sum 变大一些。
"""


class Solution:
    def twoSum(self, nums, target):
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]
        return []
