"""
N 皇后: n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

example:
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

解法：对于任意(x,y),如果要让新的点和它不能处于同一条横行、纵行或斜线上，则新点(p,q)必须要满足p+q != x+y 和p-q!= x-y,
     前者针对左下右上斜线，后者针对左上右下斜线，两者同时都保证了不在同一条横行和纵行上。
"""



class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # col_per_row: 每一行皇后的column位置组成的列表
        # cur_row：目前正在判断的row的index
        # xy_diff：所有x - y组成的列表
        # xy_sum：所有x + y组成的列表
        def dfs(col_per_row, xy_diff, xy_sum):
            cur_row = len(col_per_row)
            if cur_row == n:
                ress.append(col_per_row)
            for col in range(n):
                if col not in col_per_row and cur_row-col not in xy_diff and cur_row+col not in xy_sum:
                    dfs(col_per_row+[col], xy_diff+[cur_row-col], xy_sum+[cur_row+col])

        ress = []
        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in res] for res in ress]


if __name__ == '__main__':
    n = 4
    s = Solution()
    print(s.solveNQueens(n))