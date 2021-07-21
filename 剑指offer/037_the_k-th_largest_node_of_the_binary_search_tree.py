"""
二叉搜索树的第k大节点: 给定一棵二叉搜索树，请找出其中第k大的节点。

解题思路：
本文解法基于此性质：二叉搜索树的中序遍历为 递增序列 。
根据以上性质，易得二叉搜索树的 中序遍历倒序 为 递减序列 。
因此，求 “二叉搜索树第 k 大的节点” 可转化为求 “此树的中序遍历倒序的第 k 个节点”。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root, k):
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)
        
        self.k = k
        dfs(root)
        return self.res
