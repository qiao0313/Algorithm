"""
排列序列: 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
1."123"
2."132"
3."213"
4."231"
5."312"
6."321"
给定 n 和 k，返回第 k 个排列。

example:
输入：n = 3, k = 3
输出："213"
"""

import math

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq, k, fact = ' ', k-1, math.factorial(n-1)
        print(seq, k, fact)
        perm = [i for i in range(1, n+1)]
        print(perm)
        for i in reversed(range(n)):
            curr = perm[int(k/fact)]
            seq += str(curr)
            print(seq)
            perm.remove(curr)
            print(perm)
            if i > 0:
                k %= fact
                fact /= i
        return seq


if __name__ == '__main__':
    n = 3
    k = 3
    s = Solution()
    print(s.getPermutation(n, k))