"""
组合总和:给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

example:
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(remain, combo, index):
            if remain == 0:
                res.append(combo)
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remain:
                    break
                dfs(remain - candidates[i], combo + [candidates[i]], i)
        candidates = list(set(candidates))
        candidates.sort()
        res = []
        dfs(target, [], 0)
        return res


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    s = Solution()
    print(s.combinationSum(candidates, target))