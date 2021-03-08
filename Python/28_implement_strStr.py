"""
实现 strStr():给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。

example:
输入: haystack = "hello", needle = "ll"
输出: 2
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l, n = len(needle), len(haystack)

        for start in range(n-l+1):
            if haystack[start:start+l] == needle:
                return start

        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    s = Solution()
    print(s.strStr(haystack, needle))