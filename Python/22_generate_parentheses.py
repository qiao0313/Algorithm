"""
括号生成:数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

example:
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.singleStr('', 0, 0, n)
        return self.res

    def singleStr(self, s, left, right, n):
        if left == n and right == n:
            self.res.append(s)
        if left < n:
            self.singleStr(s + '(', left + 1, right, n)
        if right < left:
            self.singleStr(s + ')', left, right + 1, n)


if __name__ == '__main__':
    n = input("please input a number(int):")
    s = Solution()
    print(s.generateParenthesis(int(n)))