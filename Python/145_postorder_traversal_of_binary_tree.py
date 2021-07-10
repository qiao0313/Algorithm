"""
二叉树的后序遍历: 给定一个二叉树，返回它的 后序 遍历。

example:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root)

        res = list()
        postorder(root)
        return res
