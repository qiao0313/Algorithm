"""
接雨水:给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

example:
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, water, min_height = 0, len(height) - 1, 0, 0
        while l < r:
            min_height = min(height[l], height[r])
            while l < r and height[l] <= min_height:
                water += min_height - height[l]
                l += 1
            while l < r and height[r] <= min_height:
                water += min_height - height[r]
                r -= 1

        return water


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    s = Solution()
    print(s.trap(height))