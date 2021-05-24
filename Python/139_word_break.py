"""
单词拆分: 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

example:
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        import functools
        def back_track(s):
            if not s:
                return True
            res = False
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    res = back_track(s[i:]) or res
            return res
        return back_track(s)


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    so = Solution()
    print(so.wordBreak(s, wordDict))