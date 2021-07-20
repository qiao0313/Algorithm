"""
二叉树中和为某一值的路径: 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

解题思路：使用回溯法解决，其包含 先序遍历 + 路径记录 两部分。
1.先序遍历： 按照 “根、左、右” 的顺序，遍历树的所有节点。
2.路径记录： 在先序遍历中，记录从根节点到当前节点的路径。当路径为 ① 根节点到叶节点形成的路径且 ② 各节点值的和等于目标值 sum 时，将此路径加入结果列表。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, sum):
        res, path = [], []
        def recur(root, tar):
            if not root:
                return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res
