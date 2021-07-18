"""
从上往下打印二叉树: 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

解题思路：
使用队列来进行层次遍历。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printFromTopToBottom(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            for _ in range(size):
                r = queue.pop(0)
                res.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)

        return res
