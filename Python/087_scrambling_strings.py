"""
扰乱字符串: 使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
1.如果字符串的长度为 1 ，算法停止
2.如果字符串的长度 > 1 ，执行下述步骤：
    在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
    随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
    在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。

给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。

example:
输入：s1 = "great", s2 = "rgeat"
输出：true
解释：s1 上可能发生的一种情形是：
"great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
"gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
"gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
"g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
"r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
"r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
算法终止，结果字符串和 s2 相同，都是 "rgeat"
这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
"""


class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        @cache
        def dfs(i1, i2, length):
            """
            第一个字符串从 i1 开始，第二个字符串从 i2 开始，子串的长度为 length，是否和谐
            """

            # 判断两个子串是否相等
            if s1[i1:i1+length] == s2[i2:i2+length]:
                return True

            # 判断是否存在字符 c 在两个子串中出现的次数不同
            if Counter(s1[i1:i1+length]) != Counter(s2[i2:i2+length]):
                return False

            # 枚举分割位置
            for i in range(1, length):
                # 不交换的情况
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                    return True
                # 交换的情况
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    return True

            return False

        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans