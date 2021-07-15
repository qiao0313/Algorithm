"""
翻转单词顺序: 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student. "，则输出"student. a am I"。

解题思路：
倒序遍历字符串 ss ，记录单词左右索引边界 i, j；
每确定一个单词的边界，则将其添加至单词列表 res；
最终，将单词列表拼接为字符串，并返回即可。
"""


class Solution:
    def reverseWord(self, s):
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1: j + 1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)


if __name__ == '__main__':
    s = "I am a student. "
    so = Solution()
    print(so.reverseWord(s))
