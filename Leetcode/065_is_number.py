"""
有效数字: 有效数字（按顺序）可以分成以下几个部分：
1.一个 小数 或者 整数
2.（可选）一个 'e' 或 'E' ，后面跟着一个 整数

小数（按顺序）可以分成以下几个部分：
1.（可选）一个符号字符（'+' 或 '-'）
2.下述格式之一:
    1.至少一位数字，后面跟着一个点 '.'
    2.至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
    3.一个点 '.' ，后面跟着至少一位数字

整数（按顺序）可以分成以下几个部分：
1.（可选）一个符号字符（'+' 或 '-'）
2.至少一位数字

部分有效数字列举如下：
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

部分无效数字列举如下：
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
"""


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip() # 去掉两端的空白符
        s = s.lower()
        if not s:
            return False
        else:
            if s[0] == ['+', '-']:
                str = s[1:] # 去掉正负号
            if 'e' in s:

                temp_list = s.split('e')
                if len(temp_list) > 2: # 字符串s中含有多于一个的’e‘,返回False
                    return False
                temp_list[0] = temp_list[0].replace('.', '', 1) # 去掉e前面的字符串中的'.'
                if len(temp_list[1]) > 0 and temp_list[1][0] in ['+', '-']: # 去掉e后面字符串中的'+'或者'-'
                    temp_list[1] = temp_list[1].replace(temp_list[1][0], '', 1)
                if temp_list[0].isnumeric() and temp_list[1].isnumeric():
                    return True
                return False
            else: # s中不含'e'
                s = s.replace('.', '', 1)
                if s.isnumeric():
                    return True
                return False


if __name__ == '__main__':
    s = "+3.14"
    so =Solution()
    print(so.isNumber(s))