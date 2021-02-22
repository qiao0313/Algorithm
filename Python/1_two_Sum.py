"""
两数之和：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
你可以按任意顺序返回答案。

example:
输入： nums = [2, 7, 11, 15], target = 9；
输出： [0, 1]；
解释： nums[0] + nums[1] = 2 + 7 = 9
"""

class Solution(object):
    def twoSum(self, nums, target):
        """"
        :type nums: List[int]
        :type target: int
        :rtype List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
            #print(lookup)
        return []

if __name__ == '__main__':
    nums = [2 ,7, 11, 15]
    target = 9
    so = Solution()
    n = so.twoSum(nums, target)
    print("结果：", n)
