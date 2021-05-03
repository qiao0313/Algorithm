"""
不同的二叉搜索树: 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

example:
输入：n = 3
输出：5
"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            s = 0
            for k in range(i):
                s += dp[k] * dp[n - k - 1]
            dp[i] = s
        return dp[-1]


if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.numTrees(n))