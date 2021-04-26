"""
搜索旋转排序数组 II: 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

example:
输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l<= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[l]: # l和mid重复, l加一
                l += 1
            elif nums[mid] == nums[r]: # mid和r重复, r减一
                r -= 1
            elif nums[mid] > nums[l]: # l到mid是有序的, 判断target是否在其中
                if nums[l] <= target < nums[mid]: # target在其中, 选择l到mid这段
                    r = mid - 1
                else: # target不在其中，扔掉l到mid这段
                    l = mid + 1
            elif nums[mid] < nums[r]: # mid到r是有序的, 判断target是否在其中
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


if __name__ == '__main__':
    nums = [2,5,6,0,0,1,2]
    target = 0
    s = Solution()
    print(s.search(nums, target))