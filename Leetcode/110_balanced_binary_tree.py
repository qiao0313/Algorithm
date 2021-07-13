"""
平衡二叉树: 给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

example:
输入：root = [3,9,20,null,null,15,7]
输出：true
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recur(root) != -1

    def recur(self, root):
        if not root:
            return 0
        left = self.recur(root.left)
        if left == -1:
            return -1
        right = self.recur(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) else -1
