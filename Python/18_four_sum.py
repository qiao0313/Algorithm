"""
四数之和:给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

example:
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if i+3 <= n-1:
                if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                    break
            if i < n-3:
                if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                    continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, n-1
                while l < r:
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif tmp > target:
                        r -= 1
                    else:
                        l += 1

        return res


if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0
    s = Solution()
    print(s.fourSum(nums, target))
