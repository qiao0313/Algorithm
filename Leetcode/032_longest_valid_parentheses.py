"""
最长有效括号:给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

example:
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

方法：栈
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(max_length, length)

        return max_length


if __name__ == '__main__':
    s = "(()"
    so = Solution()
    print(so.longestValidParentheses(s))
