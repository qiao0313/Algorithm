"""
重建二叉树: 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        def recur(root, left, right):
            # 当前根的的索引, 递归树的左边界, 递归树的右边界
            if left > right:
                return
            node = TreeNode(preorder[root])
            i = dic[preorder[root]]
            # 左子树的根的索引为先序中的根节点+1
            # 递归左子树的左边界为原来的中序left
            # 递归左子树的右边界为中序中的根节点索引-1
            node.left = recur(root + 1, left, i - 1)
            # 右子树的根的索引为先序中的 当前根位置 + 左子树的数量 + 1
            # 递归右子树的左边界为中序中当前根节点+1
            # 递归右子树的有边界为中序中原来右子树的边界
            node.right = recur(i - left + root + 1, i + 1, right)
            return node

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        return recur(0, 0, len(inorder) - 1)
