"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

example:
输入: [1,3,5,6], 5
输出: 2
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(">>> %s: %s[%s], %s[%s], %s[%s]" % (target, nums[left], left, nums[right], right, nums[mid], mid))
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                break

        mid = mid+1 if left > mid else mid
        print("结果：", mid, left)
        return mid


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    s = Solution()
    print(s.searchInsert(nums, target))