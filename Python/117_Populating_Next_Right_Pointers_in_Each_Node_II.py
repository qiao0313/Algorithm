"""
填充每个节点的下一个右侧节点指针 II: 给定一个二叉树
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

example:
输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        dummy_left_node = Node()
        pre = dummy_left_node
        current_node = root

        while current_node:
            if current_node.left:
                pre.next = current_node.left
                pre = pre.next
            if current_node.right:
                pre.next = current_node.right
                pre = pre.next

            current_node = current_node.next

            if not current_node:
                current_node = dummy_left_node.next
                dummy_left_node.next = None
                pre = dummy_left_node
        return root
