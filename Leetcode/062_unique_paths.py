"""
不同路径: 一个机器人位于一个 m x n 网格的左上角。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
问总共有多少条不同的路径？

example:
输入：m = 3, n = 7
输出：28
"""

import math

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # def factorial(num):
        #     res = 1
        #     for i in range(1, num+1):
        #         res *= i
        #     return  res

        return math.factorial(m+n-2)/math.factorial(n-1)/math.factorial(m-1)


if __name__ == '__main__':
    m = 3
    n = 7
    s = Solution()
    print(s.uniquePaths(m, n))