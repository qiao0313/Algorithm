"""
从中序与后序遍历序列构造二叉树: 根据一棵树的中序遍历与后序遍历构造二叉树。

example:
输入：中序遍历 inorder = [9,3,15,20,7]
     后序遍历 postorder = [9,15,7,20,3]
输出：
   3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not (inorder and postorder):
            return None
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        k = inorder.index(rootVal)
        root.left = self.buildTree(inorder[:k], postorder[:k])
        root.right = self.buildTree(inorder[k + 1:], postorder[k:-1])
        return root