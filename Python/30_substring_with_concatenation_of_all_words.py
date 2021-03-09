"""
串联所有单词的子串:给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

examples:
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
"""


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        res = []
        if len(words) == 0 or len(s) < len(words) * len(words[0]):
            return res
        n , m, wl = len(s), len(words), len(words[0])
        maps, cur_map = {}, {}
        maps = Counter(words)
        for i in range(wl):
            count, start, r = 0, i, i
            while r + wl <= n:
                string = s[r:r+wl]
                if string in maps:
                    cur_map[string] = cur_map.get(string, 0) + 1
                    if cur_map[string] <= maps[string]:
                        count += 1
                    while cur_map[string] > maps[string]:
                        tmp = s[start:start+wl]
                        cur_map[tmp] -= 1
                        start += wl
                        if cur_map[tmp] < maps[tmp]:
                            count -= 1
                    if count == m:
                        res.append(start)
                        tmp = s[start:start+wl]
                        cur_map[tmp] -= 1
                        start += wl
                        count -= 1
                else:
                    cur_map = {}
                    count = 0
                    start = r + wl
                r += wl
            cur_map = {}
        return res

if __name__ == '__main__':
    #s = "barfoothefoobarman"
    #words = ["foo", "bar"]
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    so = Solution()
    print(so.findSubstring(s, words))