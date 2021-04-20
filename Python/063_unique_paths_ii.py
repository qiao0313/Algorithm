"""
不同路径 II: 一个机器人位于一个 m x n 网格的左上角。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。

example：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""


class Solution:
    def uniquePathswithObstackles(self, obstacleGrid):
        if (obstacleGrid == None or len(obstacleGrid) == 0):
            return 0

        # 定义dp数组并初始化第1行和第1列
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        i, j = 0, 0
        while i < m and obstacleGrid[i][0] == 0:
            dp [i][0] = 1
            i += 1
        while j < n and obstacleGrid[0][j] == 0:
            dp [0][j] = 1
            j += 1
        # print(dp)
        # 根据状态转移方程 dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 进行递推
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[m-1][n-1]

if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    s = Solution()
    print(s.uniquePathswithObstackles(obstacleGrid))