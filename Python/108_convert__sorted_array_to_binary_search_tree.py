"""
将有序数组转换为二叉搜索树: 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

example:
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(nums, lo, hi):
            if lo > hi:
                return None

            # 以升序数组的中间元素作为根节点 root
            mid = lo + (hi - lo) / 2
            root = TreeNode(nums[mid])
            # 递归的构建 root 的左子树与右子树
            root.left = dfs(nums, lo, mid - 1)
            root.right = dfs(nums, mid + 1, hi)

            return root

        return dfs(nums, 0, len(nums) - 1)