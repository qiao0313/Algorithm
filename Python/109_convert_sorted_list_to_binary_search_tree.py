"""
有序链表转换二叉搜索树: 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

example:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
     0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def getLength(head):
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret

        def buildTree(left, right):
            if left == right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = TreeNode(mid + 1, right)
            return root

        length = getLength(head)
        return buildTree(0, length - 1)