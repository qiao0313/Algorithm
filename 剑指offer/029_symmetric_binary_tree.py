"""
对称的二叉树: 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

解题思路：
对称二叉树定义： 对于树中 任意两个对称节点 L 和 R ，一定有：
    L.val=R.val ：即此两对称节点值相等。
    L.left.val=R.right.val ：即 LL 的 左子节点 和 RR 的 右子节点 对称；
    L.right.val=R.left.val ：即 LL 的 右子节点 和 RR 的 左子节点 对称。
根据以上规律，考虑从顶至底递归，判断每对节点是否对称，从而判断树是否为对称二叉树。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True
