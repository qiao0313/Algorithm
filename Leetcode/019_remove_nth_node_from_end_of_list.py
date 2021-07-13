"""
删除链表的倒数第 N 个结点:给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

example:
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
"""


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
