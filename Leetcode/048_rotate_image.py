"""
旋转图像: 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

example:
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]

        先上下翻转，然后中心对称翻转：
        1.上下翻转规律 [i][:] --> [n-1-i][:]
        2.对角线变换的规律是 [i][j] --> [j][i]

        1 1 1    3 3 3    3 2 1
        2 2 2 -> 2 2 2 -> 3 2 1
        3 3 3    1 1 1    3 2 1
        """
        n = len(matrix)
        #上下翻转
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        #主对角线翻转
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    print(s.rotate(matrix))