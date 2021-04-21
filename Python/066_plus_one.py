"""
加一: 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

example:
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
"""


class Solution:
    def pulsOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry  = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
                break
            else:
                digits[i] -= 10
        if carry == 1:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    digits = [1, 2, 3]
    s = Solution()
    print(s.pulsOne(digits))