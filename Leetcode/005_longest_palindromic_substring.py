"""
最长回文子串:给你一个字符串 s，找到 s 中最长的回文子串。
如果一个字符串从左向右写和从右向左写是一样的，这样我们就把它叫做回文字符串。

example:
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        m, l, r = 0, 0, 0

        for i in range(n):
            #odd case
            for j in range(min(i+1, n-i)):
                if s[i-j] != s[i+j]:
                    break
                if 2 * j + 1 > m:
                    m = 2 * j + 1
                    l = i - j
                    r = i + j

            if i + 1 < n and s[i] == s[i+1]:
                for j in range(min(i+1, n-i-1)):
                    if s[i-j] != s[i+j+1]:
                        break
                    if 2 * j + 2 > m:
                        m = 2 * j + 2
                        l = i - j
                        r = i + j +1

        return s[l:r+1]

if __name__ == '__main__':
    str = "babad"
    s = Solution()
    lp = s.longestPalindrome(str)
    print(lp)
