"""
编辑距离: 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：
1.插入一个字符
2.删除一个字符
3.替换一个字符

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 or len(word2) == 0:  # corner cases
            return max(len(word1), len(word2))

        # 初始化一个 len(word1)+1 * len(word2)+1 的矩阵
        matrix = [[i+j for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        # print(matrix)
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    d = 0
                else:
                    d = 1
                matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+d)
        # print(matrix)
        return matrix[-1][-1]


if __name__ == '__main__':
    word1, word2 = 'horse', 'ros'
    s = Solution()
    print(s.minDistance(word1, word2))