"""
二叉树的最小深度: 给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

example:
输入：root = [3,9,20,null,null,15,7]
输出：2
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            if root.left == None:
                return 1 + self.minDepth(root.right)
            if root.right == None:
                return 1 + self.minDepth(root.left)
            else:
                return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
