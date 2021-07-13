"""
第一个只出现一次的字符位置: 在一个字符串中找到第一个只出现一次的字符，并返回它的位置。字符串只包含 ASCII 码字符。
Input: abacc
Output: b

解题思路：
最直观的解法是使用 HashMap 对出现次数进行统计：字符做为 key，出现次数作为 value，遍历字符串每次都将 key 对应的 value 加 1。
最后再遍历这个 HashMap 就可以找出出现次数为 1 的字符。

考虑到要统计的字符范围有限，也可以使用整型数组代替 HashMap。ASCII 码只有 128 个字符，因此可以使用长度为 128 的整型数组来存储每个字符出现的次数。

以上实现的空间复杂度还不是最优的。考虑到只需要找到只出现一次的字符，那么需要统计的次数信息只有 0,1,更大，使用两个比特位就能存储这些信息。
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1

        store = {}
        lis = list(s)

        for i in lis:
            if i not in store.keys():
                store[i] = 0
            store[i] += 1

        for i in lis:
            if store[i] == 1:
                return s.index(i)

        return -1

if __name__ == '__main__':
    s = "abacc"
    so = Solution()
    print(so.FirstNotRepeatingChar(s))
