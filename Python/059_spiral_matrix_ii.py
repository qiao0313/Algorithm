"""
螺旋矩阵 II: 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

example:
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
"""


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        curNum = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        maxUp = maxLeft = 0
        maxDown = maxRight = n-1
        diretion = 0
        while True:
            if diretion == 0:#go right
                for i in range(maxLeft, maxRight+1):
                    curNum += 1
                    matrix[maxUp][i] = curNum
                maxUp += 1
            elif diretion == 1:# go down
                for i in range(maxUp, maxDown+1):
                    curNum += 1
                    matrix[i][maxRight] = curNum
                maxRight -= 1
            elif diretion == 2:# go left
                for i in reversed(range(maxLeft, maxRight+1)):
                    curNum += 1
                    matrix[maxDown][i] = curNum
                maxDown -= 1
            else:#go up
                for i in reversed(range(maxUp, maxDown+1)):
                    curNum += 1
                    matrix[i][maxLeft] = curNum
                maxLeft += 1
            if curNum >= n*n:
                return matrix
            diretion = (diretion + 1) % 4


if __name__ == '__main__':
    n = 4
    s = Solution()
    print(s.generateMatrix(n))