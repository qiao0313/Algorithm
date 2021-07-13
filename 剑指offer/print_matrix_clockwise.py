"""
顺时针打印矩阵: 按顺时针的方向，从外到里打印矩阵的值。

解题思路：
一层一层从外到里打印，观察可知每一层打印都有相同的处理步骤，唯一不同的是上下左右的边界不同了。因此使用四个变量 r1, r2, c1, c2 分别
存储上下左右边界值，从而定义当前最外层。打印当前最外层的顺序：从左到右打印最上一行->从上到下打印最右一行->从右到左打印最下一
行->从下到上打印最左一行。应当注意只有在 r1 != r2 时才打印最下一行，也就是在当前最外层的行数大于 1 时才打印最下一行，这是因为当前
最外层只有一行时，继续打印最下一行，会导致重复打印。打印最左一行也要做同样处理。
"""


class Solution:
    def printMatrix(self, matrix):
        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        result = []
        while rows > start * 2 and cols > start * 2:
            self.PrintMatrixInCircle(matrix, cols, rows, start, result)
            start += 1
        return result

    def PrintInMatrixCircle(self, matrix, cols, rows, start, result):
        endX = cols - 1 - start
        endY = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, endX+1):
            result.append(matrix[start][i])

        # 从上到下打印一行
        if start < endY:
            for i in range(start+1, endY+1):
                result.append(matrix[i][endX])

        # 从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                result.append(matrix[endY][i])

        # 从下到上打印一行
        if start < endX and start < endY-1:
            for i in range(endY-1, start, -1):
                result.append(matrix[i][start])