"""
字符串转换整数 (atoi):请你来实现一个 myAtoi(string s) 函数，
使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：
1.读入字符串并丢弃无用的前导空格
2.检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。
确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
3.读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
4.将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。
如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
5.如果整数数超过 32 位有符号整数范围 [−2^31, 2^31 − 1] ，需要截断这个整数，
使其保持在这个范围内。具体来说，小于 −2^31 的整数应该被固定为 −2^31 ，
大于 2^31− 1 的整数应该被固定为 2^31− 1 。返回整数作为最终结果。

example:
输入：s = "42"
输出：42
"""

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        strNum = 0
        if len(str) == 0:
            return strNum

        positive = True
        if str[0] == '+' or str[0] == '-':
            if str[0] == '-':
                positive = False
            str = str[1:]

        for char in str:
            if char >= '0'and char <= '9':
                # ord()返回对应字符的ASCII数值
                strNum = strNum * 10 + ord(char) - ord('0')
            if char < '0' or char >'9':
                break

        if strNum > 2147483647:
            if positive == False:
                return -2147483648
            else:
                return 2147483647

        if not positive:
            strNum = 0 - strNum

        return strNum

if __name__ == '__main__':
    #str = "4193 with words"
    str = "   -42"
    s = Solution()
    x = s.myAtoi(str)
    print(x)
