"""
插入区间: 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

examples:
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
"""


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
            # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
            # 与插入区间有交集，计算它们的并集
                left = min(li, left)
                right = max(ri, right)
        if not placed:
            ans.append([left, right])
        return ans


if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    s = Solution()
    print(s.insert(intervals, newInterval))