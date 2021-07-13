"""
螺旋矩阵: 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

example:
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r, i, j ,di, dj = [], 0, 0, 0, 1
        if matrix != []:
            for _ in range(len(matrix) * len(matrix[0])):
                r.append(matrix[i][j])
                matrix[i][j] = 0
                if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
                    di, dj = dj, -di
                i += di
                j += dj
                # print(i, j, di, dj)
                # print(matrix)
                # print(r)
        return r


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    print(s.spiralOrder(matrix))