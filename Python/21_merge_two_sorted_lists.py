"""
合并两个有序链表:将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

example:
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""


class Solution:
    def mergeTwoList(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListMode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        dummy = ListNode(-1)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2

        return dummy.next