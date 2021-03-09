"""
两数相除:给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

example:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
"""


def div(a, b):
    if a < b:
        return 0
    count = 1
    tb = b
    while tb + tb < a:
        count = count + count  # 最小解翻倍
        tb = tb + b  # 当前测试的值也翻倍

    return count + div(a - tb, b)

class Solution:
    def divide(self, dividend:int, divisor:int):
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend

        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        a = dividend if dividend > 0 else -dividend
        b = divisor if divisor > 0 else -divisor
        res = div(a, b)
        if sign > 0:
            return res
        else:
            return -res


if __name__ == '__main__':
    dividend = 10
    divisor = 3
    s = Solution()
    print(s.divide(dividend, divisor))