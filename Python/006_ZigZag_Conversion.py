"""
Z 字形变换:将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

example:
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        idx, step = 0, 1

        for x in s:
            res[idx] += x
            print(idx, step, res)
            if idx == 0:  ## 第一行，一直向下走
                step = 1
            elif idx == numRows - 1:  ## 最后一行了，向上走
                step = -1
            idx += step
        return ''.join(res)

if __name__ == '__main__':
    str = "PAYPALISHIRING"
    numRows = 3
    s = Solution()
    zz = s.convert(str, numRows)
    print(zz)
