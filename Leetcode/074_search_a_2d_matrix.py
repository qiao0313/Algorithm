"""
搜索二维矩阵: 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
1.每行中的整数从左到右按升序排列。
2.每行的第一个整数大于前一行的最后一个整数。

example:
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        l, r = 0, row-1
        while l <= r:
            mid_row = l + ((r-l)>>2)
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                m, n = 0, col-1
                while m <= n:
                    mid_col = m + ((n-m)>>2)
                    if matrix[mid_row][mid_col] > target:
                        n = mid_col-1
                    elif matrix[mid_row][mid_col] < target:
                        m = mid_col+1
                    else:
                        return True
                return False
            elif target < matrix[mid_row][0]:
                r = mid_row-1
            else:
                l = mid_row+1
        return False


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    s = Solution()
    print(s.searchMatrix(matrix, target))