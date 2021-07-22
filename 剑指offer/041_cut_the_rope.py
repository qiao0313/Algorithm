"""
剪绳子: 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

解题思路：
设将长度为 n 的绳子切为 a 段：n=n1+n2+...+na，本题等价于求解：max(n1×n2×...×na)。
推论一： 将绳子 以相等的长度等分为多段 ，得到的乘积最大。
推论二： 尽可能将绳子以长度 33 等分为多段时，乘积最大。
"""


import math

class Solution:
    def cuttingRope(self, n):
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a-1) * 4)
        return int(math.pow(3, a) * 2)
