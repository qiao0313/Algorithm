"""
两两交换链表中的节点:给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

example:
输入：head = [1,2,3,4]
输出：[2,1,4,3]
"""


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(head.next.next)
        tmp.next = head
        return tmp
