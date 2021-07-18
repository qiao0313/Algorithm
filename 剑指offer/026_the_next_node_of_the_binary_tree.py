"""
二叉树的下一个结点: 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回 。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

解题思路：
中序遍历的过程：先遍历树的左子树，再遍历根节点，最后再遍历右子树。所以最左节点是中序遍历的第一个节点。
1.如果一个节点的右子树不为空，那么该节点的下一个节点是右子树的最左节点；
2.否则，向上找第一个左链接指向的树包含该节点的祖先节点。
"""


class Solution:
    def getNext(self, pNode):
        if pNode.right != None:
            node = pNode.right
            while node.left != None:
                node = node.left
            return node
        else:
            while pNode.next != None:
                parent = pNode.next
                if parent.left == pNode:
                    return parent
                pNode = pNode.next

        return None
