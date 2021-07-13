"""
最长公共前缀:编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

example:
输入：strs = ["flower","flow","flight"]
输出："fl"
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        dp = [strs[0]] * len(strs)
        for i in range(1, len(strs)):
            while not strs[i].startswith(dp[i-1]):
                dp[i-1] = dp[i-1][:-1]
            dp[i] = dp[i-1]
        return dp[-1]

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
