"""
N皇后 II: n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

example:
输入：n = 4
输出：2
"""


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(col_per_row, xy_diff, xy_sum):
            cur_row = len(col_per_row)
            if cur_row == n:
                ress.append(col_per_row)
            for col in range(n):
                if col not in col_per_row and cur_row-col not in xy_diff and cur_row+col not in xy_sum:
                    dfs(col_per_row+[col], xy_diff+[cur_row-col], xy_sum+[cur_row+col])

        ress = []
        dfs([], [], [])
        return len(ress)


if __name__ == '__main__':
    n = 4
    s = Solution()
    print(s.totalNQueens(n))