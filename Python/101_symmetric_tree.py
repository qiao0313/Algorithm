"""
对称二叉树: 给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
class Solution1:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            return check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)

# 迭代
class Solution2:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or not (root.left or root.right):
            return True
        # 用队列保存节点
        queue = [root.left, root.right]
        while queue:
            # 从队列中取出两个节点，再比较这两个节点
            left = queue.pop(0)
            right = queue.pop(0)
            # 如果两个节点都为空就继续循环，两者有一个为空就返回false
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            # 将左节点的左孩子， 右节点的右孩子放入队列
            queue.append(left.left)
            queue.append(right.right)
            # 将左节点的右孩子，右节点的左孩子放入队列
            queue.append(left.right)
            queue.append(right.left)
        return True
