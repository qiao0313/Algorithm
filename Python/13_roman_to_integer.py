"""
examples:
输入: "IV"
输出: 4

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
"""
class Solution:
    def romanToInteger(self, s):
        """
        :ptype s: str
        :rtype: int
        """
        lookup = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        res = 0
        for i in range(len(s)):
            if i > 0 and lookup[s[i]] > lookup[s[i-1]]:
                res = res + lookup[s[i]] - 2 * lookup[s[i-1]]
            else:
                res += lookup[s[i]]

        return res

if __name__ == '__main__':
    s = 'IV'
    so = Solution()
    x = so.romanToInteger(s)
    print(x)