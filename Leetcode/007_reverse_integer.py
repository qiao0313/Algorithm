"""
整数反转：给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−2^31, 2^31 − 1] ，就返回 0。

examples:
输入：x = 123
输出：321

输入：x = -123
输出：-321

输入：x = 120
输出：21

注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]
根据这个假设，如果反转后的整数溢出，则返回 0
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mark = 1 if x >= 0 else -1
        x_abs = abs(x)
        result = mark * int(str(x_abs)[::-1])
        return result if -2**31 <= result <= 2**31-1 else 0


if __name__ == '__main__':
    x = -12395
    s = Solution()
    r = s.reverse(x)
    print(r)
