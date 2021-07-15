"""
字符流中第一个不重复的字符: 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符 "go" 时，第一个只出现一次的字符是 "g"。
当从该字符流中读出前六个字符“google" 时，第一个只出现一次的字符是 "l"。

解题思路：
使用统计数组来统计每个字符出现的次数，本题涉及到的字符为都为 ASCII 码，因此使用一个大小为 128 的整型数组就能完成次数统计任务。
使用队列来存储到达的字符，并在每次有新的字符从字符流到达时移除队列头部那些出现次数不再是一次的元素。因为队列是先进先出顺序，因
此队列头部的元素为第一次只出现一次的字符。
"""


class Solution:
    def __init__(self):
        self.dic = {}
        self.lis = []

    def firstApperingOnce(self):
        while len(self.lis) > 0 and self.dic[self.lis[0]] == 2:
            self.lis.pop(0)
        if len(self.lis) == 0:
            return '#'
        else:
            return self.lis[0]

    def insert(self, char):
        if char not in self.dic.keys():
            self.dic[char] = 1
            self.lis.append(char)
        elif self.dic[char]:
            self.dic[char] = 2
