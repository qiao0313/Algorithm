"""
组合总和 II:给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。

example:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[List[int]]
        :ptype target: int
        :rtype: List[List[int]]
        """
        def dfs(remain, combo, index):
            if remain == 0 and combo not in res:
                res.append(combo)
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remain:
                    break
                dfs(remain - candidates[i], combo + [candidates[i]], i+1)
        candidates.sort()
        res = []
        dfs(target, [], 0)
        return res


if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    s = Solution()
    print(s.combinationSum2(candidates, target))