"""
翻转字符串里的单词: 给你一个字符串 s ，逐个翻转字符串中的所有 单词 。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

example:
输入：s = "the sky is blue"
输出："blue is sky the"
"""

import collections


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(reversed(s.split()))


class Solution:
    def reverseWord(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1

        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = collections.deque(), []
        # 将单词 push 到队列的头部
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)


if __name__ == '__main__':
    s = "the sky is blue"
    so = Solution()
    print(so.reverseWord(s))