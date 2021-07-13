"""
逆波兰表达式求值: 根据 逆波兰表示法，求表达式的值。
有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

example:
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
"""


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op_to_binary_fn = {
            "+": lambda x, y: int(x + y),
            "-": lambda x, y: int(x - y),
            "*": lambda x, y: int(x * y),
            "/": lambda x, y: int(x / y),  # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)

        return stack[0]


if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    s = Solution()
    print(s.evalRPN(tokens))