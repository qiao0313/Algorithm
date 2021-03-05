"""
最接近的三数之和:给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

example:
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n, res, diff = len(nums), None, float('inf')
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l ,r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return target
                elif tmp > target:
                    r -= 1
                    if abs(tmp-target) < diff:
                        diff = abs(tmp-target)
                        res = tmp
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    if abs(tmp-target) < diff:
                        diff = abs(tmp-target)
                        res = tmp
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res


if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    s = Solution()
    print(s.threeSumClosest(nums, target))