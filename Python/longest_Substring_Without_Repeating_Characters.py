"""
无重复字符的最长子串:给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

example:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, start, n = 0, 0, len(s)
        maps = {}
        for i in range(n):
            start = max(start, maps.get(s[i], -1)+1)
            l = max(l, i - start+1)
            maps[s[i]] = i
        return l

if __name__ == '__main__':
    s = Solution()
    l = s.lengthOfLongestSubstring("abcabcbb")
    print(l)