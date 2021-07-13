"""
直线上最多的点数: 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

example:
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
"""


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        ans = 1
        for i in range(n):
            x = points[i]
            for j in range(i+1, n):
                y = points[j]
                cnt = 2
                for k in range(j+1, n):
                    p = points[k]
                    s1 = (y[1] - x[1]) * (y[0] - x[0])
                    s2 = (p[1] - p[1]) * (y[0] - y[0])
                    if s1 == s2:
                        cnt += 1
                ans = max(ans, cnt)

        return ans