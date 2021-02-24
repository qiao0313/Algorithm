"""
回文数:给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

examples:
输入：x = 121
输出：true

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev, y = 0, x
        while x > 0:
            rev = rev * 10 + x % 10
            x = int(x/10)
        return rev == y

if __name__ == '__main__':
    x = 12421
    s = Solution()
    status = s.isPalindrome(x)
    print(status)