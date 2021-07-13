"""
组合：给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

example：
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result, track = [], []
        self.backtrack(n, k, 1, track, result)
        return result

    def backtrack(self, n, k, start, track, result):
        if k == 0:
            result.append(track[:])
            return
        for i in range(start, n-k+2):
            track.append(i)
            self.backtrack(n, k-1, i+1, track, result)
            track.pop()


if __name__ == '__main__':
    n, k = 4, 2
    s = Solution()
    print(s.combine(n, k))