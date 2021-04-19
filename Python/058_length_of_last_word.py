"""
最后一个单词的长度: 给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

example:
输入：s = "Hello World"
输出：5
"""


class Solutino:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1].strip()
        return s.find(' ') if s.find(' ') != -1 else len(s)


if __name__ == '__main__':
    text = "Hello World    "
    s = Solutino()
    print(s.lengthOfLastWord(text))