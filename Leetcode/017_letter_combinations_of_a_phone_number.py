"""
电话号码的字母组合:给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

example:
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        self.res = []
        self.singleResult('', digits)
        return self.res

    def singleResult(self, s, digits):
        if len(digits) == 0:
            self.res.append(s)
        else:
            mapx = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}
            cur_digit = digits[0]
            for c in mapx[cur_digit]:
                self.singleResult(s + c, digits[1:])


if __name__ == '__main__':
    digits = '23'
    s = Solution()
    print(s.letterCombinations(digits))
