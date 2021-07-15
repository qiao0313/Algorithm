"""
包含min函数的栈: 实现一个包含 min() 函数的栈，该方法返回当前栈中最小的值。

解题思路：
使用一个额外的 minStack，栈顶元素为当前栈中最小的值。在对栈进行 push 入栈和 pop 出栈操作时，同样需要对 minStack 进行入栈出栈操
作，从而使 minStack 栈顶元素一直为当前栈中最小的值。在进行 push 操作时，需要比较入栈元素和当前栈中最小值，将值较小的元素 push 到
minStack 中。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)

    def pop(self):
        if self.stack == None or self.minStack == None:
            return None
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minStack[-1]