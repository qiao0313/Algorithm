"""
验证回文串: 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

example:
输入: "A man, a plan, a canal: Panama"
输出: true
"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1

        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    so = Solution()
    print(so.isPalindrome(s))