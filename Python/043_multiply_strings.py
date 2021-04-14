"""
字符串相乘: 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

example:
输入: num1 = "123", num2 = "456"
输出: "56088"
"""


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        lookup = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                  "9": 9}  # 节省查找时间，避免无休止使用ord函数来得到数字
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]

        tmp_res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp_res[i + j] += lookup[num1[i]] * lookup[num2[j]]

        # print(tmp_res)

        res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1) + len(num2)):
            res[i] = tmp_res[i] % 10
            if i < len(num1) + len(num2) - 1:
                tmp_res[i + 1] += tmp_res[i] // 10

        # print(tmp_res)
        # print(res)
        return ''.join(str(i) for i in res[::-1]).lstrip('0')  # 去掉最终结果头部可能存在的‘0’


if __name__ == '__main__':
    num1 = '123'
    num2 = '456'
    s = Solution()
    print(s.multiply(num1, num2))