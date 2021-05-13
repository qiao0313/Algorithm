"""
杨辉三角 II: 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

example:
输入: 3
输出: [1,3,3,1]
"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        res = [1]
        for i in range(1, rowIndex + 1):
            tmp = [1]
            for j in range(1, i):
                tmp.append(res[j - 1] + res[j])
            tmp.append(1)
            # print(tmp)
            res = tmp
        return res

if __name__ == '__main__':
    rowIndex = 4
    s = Solution()
    print(s.getRow(rowIndex))