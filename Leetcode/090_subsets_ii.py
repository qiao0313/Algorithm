"""
子集 II: 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

example:
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
"""

class Solution:
    def subsetWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]

        for i in range(len(nums)):
            print(i)
            if any(nums[i] in tmp for tmp in res):
                res.extend([tmp + [nums[i]] for tmp in res if tmp.count(nums[i]) == i - nums.index(nums[i])])
            else:
                res.extend([tmp + [nums[i]] for tmp in res])
            print(res)
        return res


if __name__ == '__main__':
    nums = [1,2,2]
    s = Solution()
    print(s.subsetWithDup(nums))