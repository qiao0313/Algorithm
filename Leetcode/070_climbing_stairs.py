"""
爬楼梯: 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

example:
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = [1, 2, 3]
        if n < 4:
            return fib[n-1]
        for k in range(3, n+1):
            fib[2] = fib[0] + fib[1]
            fib[0], fib[1] = fib[1], fib[2]
        return fib[2]


if __name__ == '__main__':
    n = 4
    s = Solution()
    print(s.climbStairs(n))