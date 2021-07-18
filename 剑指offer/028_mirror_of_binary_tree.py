"""
二叉树的镜像: 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

解题思路：
1.递归：根据二叉树镜像的定义，考虑递归遍历（dfs）二叉树，交换每个节点的左 / 右子节点，即可生成二叉树的镜像。
2.辅助栈（或队列）:利用栈（或队列）遍历树的所有节点 node，并交换每个 node 的左 / 右子节点。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def mirrorTree(self, root):
        if not root:
            return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

class Solution2:
    def mirrorTree(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
