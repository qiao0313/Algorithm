"""
数组中重复的数字: 在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字是重复的，
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。

解题思路：要求时间复杂度 O(N)，空间复杂度 O(1)。因此不能使用排序的方法，也不能使用额外的标记数组。
对于这种数组元素在 [0, n-1] 范围内的问题，可以将值为 i 的元素调整到第 i 个位置上进行求解。在调整过程中，如果第 i 位置上已经有一个值为 i 的元素，就可以知道 i 值重复。
以 (2, 3, 1, 0, 2, 5) 为例，遍历到位置 4 时，该位置上的数为 2，但是第 2 个位置上已经有一个 2 的值了，因此可以知道 2 重复。

example:
Input:
[2, 3, 1, 0, 2, 5]
Output:
2
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    def duplicate(self, nums):
        if not nums or len(nums) < 0:
            return False
        for i in nums:
            if i < 0 or i > len(nums) - 1:
                return False
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                self.swap(nums, i, nums[i])
            self.swap(nums, i, nums[i])
        return -1

    def swap(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5]
    s = Solution()
    print(s.duplicate(nums))
