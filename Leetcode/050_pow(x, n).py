"""
Pow(x, n): 实现 pow(x, n) ，即计算 x 的 n 次幂函数。

example:
输入：x = 2.00000, n = -2
输出：0.25000
"""


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            # if n & 1:
            if (n % 2 != 0):
                pow *= x
            x *= x
            # n >>= 1
            n //= 2
        return pow

if __name__ == '__main__':
    x = 2.00000
    n = -2
    s = Solution()
    print(s.myPow(x, n))